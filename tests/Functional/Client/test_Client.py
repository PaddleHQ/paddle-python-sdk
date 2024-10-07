from json import loads, dumps
from pytest import mark, raises
from urllib.parse import unquote
import requests

from paddle_billing.Exceptions.ApiError import ApiError
from paddle_billing.Exceptions.ApiErrors.AddressApiError import AddressApiError

from requests.exceptions import RequestException, HTTPError

from tests.Utils.TestLogger import LogHandler
from tests.Utils.TestClient import TestClient as UtilsTestClient


class TestClient:
    @mark.parametrize(
        [
            "expected_response_status",
            "expected_reason",
            "expected_response_body",
            "expected_exception",
        ],
        [
            (
                400,
                "Bad Request",
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
            ),
            (
                404,
                "Not Found",
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
            ),
            (
                400,
                "Bad Request",
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
            ),
        ],
        ids=[
            "Returns bad_request response",
            "Returns not_found response",
            "Returns address_location_not_allowed response",
        ],
    )
    def test_post_raw_returns_error_response(
        self,
        test_client,
        test_log_handler: LogHandler,
        mock_requests,
        expected_response_status,
        expected_reason,
        expected_response_body,
        expected_exception,
    ):
        expected_request_url = f"{test_client.base_url}/some/url"
        expected_request_body = {"some_property": "some value"}
        mock_requests.post(
            expected_request_url,
            status_code=expected_response_status,
            text=dumps(expected_response_body),
            reason=expected_reason,
        )

        with raises(expected_exception) as exception_info:
            test_client.client.post_raw(expected_request_url, expected_request_body)

        request_json = test_client.client.payload
        last_request = mock_requests.last_request
        api_error = exception_info.value

        assert (
            unquote(last_request.url) == expected_request_url
        ), "The URL does not match the expected URL, verify the query string is correct"

        assert loads(request_json) == expected_request_body, "The request JSON doesn't match the expected fixture JSON"

        assert isinstance(api_error, ApiError)
        assert isinstance(api_error, HTTPError)
        assert isinstance(api_error, RequestException)
        assert api_error.response.status_code == expected_response_status, "Unexpected status code"
        assert api_error.error_type == expected_response_body["error"]["type"]
        assert api_error.error_code == expected_response_body["error"]["code"]
        assert api_error.detail == expected_response_body["error"]["detail"]
        assert api_error.docs_url == expected_response_body["error"]["documentation_url"]

        if "errors" in expected_response_body["error"]:
            assert len(api_error.field_errors) == len(expected_response_body["error"]["errors"])

            for i, expected_field_error in enumerate(expected_response_body["error"]["errors"]):
                assert api_error.field_errors[i].field == expected_field_error["field"]
                assert api_error.field_errors[i].error == expected_field_error["message"]
        else:
            assert len(api_error.field_errors) == 0

        assert str(api_error) == expected_response_body["error"]["detail"]
        assert repr(api_error) == (
            "ApiError("
            f"error_type='{api_error.error_type}', "
            f"error_code='{api_error.error_code}', "
            f"detail='{api_error.detail}', "
            f"docs_url='{api_error.docs_url}', "
            f"field_errors={api_error.field_errors}"
            ")"
        )

        assert (
            test_log_handler.get_logs()[0].message
            == f"Request failed: {expected_response_status} Client Error: {expected_reason} for url: {expected_request_url}. {api_error.detail}"
        )

    def test_client_with_custom_timeout(self, mock_requests):
        test_client = UtilsTestClient(timeout=99)

        expected_request_url = f"{test_client.base_url}/some/url"

        mock_requests.post(expected_request_url, status_code=200)

        test_client.client.post_raw(expected_request_url)

        assert mock_requests.last_request.timeout == 99

    def test_client_default_timeout(self, test_client, mock_requests):
        expected_request_url = f"{test_client.base_url}/some/url"

        mock_requests.post(expected_request_url, status_code=200)

        test_client.client.post_raw(expected_request_url)

        assert mock_requests.last_request.timeout == 60.0

    def test_client_throws_connection_error(self, test_client, mock_requests):
        expected_request_url = f"{test_client.base_url}/some/url"

        mock_requests.post(expected_request_url, exc=requests.exceptions.ConnectionError("Some Connection Error"))

        with raises(requests.exceptions.ConnectionError) as exception_info:
            test_client.client.post_raw(expected_request_url)

        exception = exception_info.value

        assert isinstance(exception, RequestException)
        assert str(exception) == "Some Connection Error"
