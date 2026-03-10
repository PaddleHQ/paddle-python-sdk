from json import loads, dumps
from pytest import mark, raises
from urllib.parse import unquote

import httpx
import respx

from paddle_billing import AsyncClient, Environment, Options
from paddle_billing.Exceptions.ApiError import ApiError
from paddle_billing.Exceptions.ApiErrors.AddressApiError import AddressApiError

from tests.Utils.AsyncTestClient import AsyncTestClient as UtilsAsyncTestClient
from tests.Utils.TestLogger import LogHandler


class TestAsyncClient:
    @mark.parametrize(
        [
            "expected_response_status",
            "expected_response_body",
            "expected_exception",
            "headers",
            "expected_retry_after",
        ],
        [
            (
                400,
                {
                    "error": {
                        "type": "request_error",
                        "code": "bad_request",
                        "detail": "Invalid request",
                        "documentation_url": "https://developer.paddle.com/v1/errors/shared/bad_request",
                        "errors": [{"field": "some_field", "message": "Some error message"}],
                    },
                    "meta": {"request_id": "f00bb3ca-399d-4686-889c-50b028f4c912"},
                },
                ApiError,
                {},
                None,
            ),
            (
                404,
                {
                    "error": {
                        "type": "request_error",
                        "code": "not_found",
                        "detail": "Entity not found",
                        "documentation_url": "https://developer.paddle.com/v1/errors/shared/not_found",
                    },
                    "meta": {"request_id": "f00bb3ca-399d-4686-889c-50b028f4c912"},
                },
                ApiError,
                {},
                None,
            ),
            (
                400,
                {
                    "error": {
                        "type": "request_error",
                        "code": "address_location_not_allowed",
                        "detail": "Cannot create address with an unsupported location",
                        "documentation_url": "https://developer.paddle.com/errors/addresses/address_location_not_allowed",
                    },
                    "meta": {"request_id": "f00bb3ca-399d-4686-889c-50b028f4c912"},
                },
                AddressApiError,
                {},
                None,
            ),
            (
                429,
                {
                    "error": {
                        "type": "request_error",
                        "code": "too_many_requests",
                        "detail": "IP address exceeded the allowed rate limit. Retry after the number of seconds in the Retry-After header.",
                        "documentation_url": "https://developer.paddle.com/errors/shared/too_many_requests",
                    },
                    "meta": {"request_id": "f00bb3ca-399d-4686-889c-50b028f4c912"},
                },
                ApiError,
                {"Retry-After": "42"},
                42,
            ),
        ],
        ids=[
            "Returns bad_request response",
            "Returns not_found response",
            "Returns address_location_not_allowed response",
            "Returns too_many_requests response",
        ],
    )
    async def test_post_raw_returns_error_response(
        self,
        async_test_client,
        test_log_handler: LogHandler,
        expected_response_status,
        expected_response_body,
        expected_exception,
        headers,
        expected_retry_after,
    ):
        expected_request_url = f"{async_test_client.base_url}/some/url"
        expected_request_body = {"some_property": "some value"}

        with respx.mock() as mock:
            mock.post(expected_request_url).respond(
                status_code=expected_response_status,
                json=expected_response_body,
                headers=headers,
            )

            with raises(expected_exception) as exception_info:
                await async_test_client.client.post_raw(expected_request_url, expected_request_body)

        request_json = async_test_client.client.payload
        api_error = exception_info.value

        assert loads(request_json) == expected_request_body, "The request JSON doesn't match the expected fixture JSON"

        assert isinstance(api_error, ApiError)
        assert api_error.response.status_code == expected_response_status, "Unexpected status code"
        assert api_error.error_type == expected_response_body["error"]["type"]
        assert api_error.error_code == expected_response_body["error"]["code"]
        assert api_error.detail == expected_response_body["error"]["detail"]
        assert api_error.docs_url == expected_response_body["error"]["documentation_url"]
        assert api_error.retry_after == expected_retry_after

        if "errors" in expected_response_body["error"]:
            assert len(api_error.field_errors) == len(expected_response_body["error"]["errors"])

            for i, expected_field_error in enumerate(expected_response_body["error"]["errors"]):
                assert api_error.field_errors[i].field == expected_field_error["field"]
                assert api_error.field_errors[i].error == expected_field_error["message"]
        else:
            assert len(api_error.field_errors) == 0

        assert str(api_error) == expected_response_body["error"]["detail"]

        log_message = test_log_handler.get_logs()[0].message
        assert log_message.startswith("Request failed:"), f"Unexpected log message: {log_message}"
        assert api_error.detail in log_message, f"Expected detail '{api_error.detail}' in log: {log_message}"

    async def test_async_client_with_custom_timeout(self, test_logger):
        test_client = UtilsAsyncTestClient(timeout=99, logger=test_logger)
        expected_request_url = f"{test_client.base_url}/some/url"

        with respx.mock() as mock:
            mock.post(expected_request_url).respond(200)

            await test_client.client.post_raw(expected_request_url)

            last_request = mock.calls.last.request
            assert last_request is not None

        assert test_client.client.timeout == 99

    async def test_async_client_default_timeout(self, async_test_client):
        expected_request_url = f"{async_test_client.base_url}/some/url"

        with respx.mock() as mock:
            mock.post(expected_request_url).respond(200)

            await async_test_client.client.post_raw(expected_request_url)

        assert async_test_client.client.timeout == 60.0

    async def test_async_client_throws_connection_error(self, async_test_client):
        expected_request_url = f"{async_test_client.base_url}/some/url"

        with respx.mock() as mock:
            mock.post(expected_request_url).mock(side_effect=httpx.ConnectError("Some Connection Error"))

            with raises(httpx.ConnectError) as exception_info:
                await async_test_client.client.post_raw(expected_request_url)

        exception = exception_info.value
        assert isinstance(exception, httpx.RequestError)
        assert "Some Connection Error" in str(exception)

    async def test_async_client_is_context_manager(self):
        async with AsyncClient(api_key="test_key", options=Options(Environment.SANDBOX)) as client:
            assert client is not None

    async def test_async_client_retries_on_server_error(self, async_test_client):
        expected_request_url = f"{async_test_client.base_url}/some/url"
        success_body = {"data": {}, "meta": {}}

        with respx.mock() as mock:
            # First two calls return 500, third succeeds
            mock.post(expected_request_url).side_effect = [
                httpx.Response(500),
                httpx.Response(500),
                httpx.Response(200, json=success_body),
            ]

            response = await async_test_client.client.post_raw(expected_request_url)

        assert response.status_code == 200
        assert async_test_client.client.status_code == 200
