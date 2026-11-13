import logging

from datetime import datetime, timezone
from json import loads
from pytest import fixture, mark, raises
from urllib.parse import unquote

from paddle_billing.Entities.ApiKey import ApiKey
from paddle_billing.Entities.ApiKeyRotation import ApiKeyRotation
from paddle_billing.Entities.ApiKeyRotationCreated import ApiKeyRotationCreated
from paddle_billing.Entities.ApiKeys import ApiKeyPermission, ApiKeyRotationStatus, ApiKeyStatus
from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Collections import ApiKeyCollection, ApiKeyRotationCollection
from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing import Environment
from paddle_billing.Json import PayloadEncoder

from paddle_billing.Resources.ApiKeys.Operations import CreateApiKeyRotation, ListApiKeyRotations, ListApiKeys
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures
from tests.Utils.TestClient import TestClient

CLIENT_API_KEY = "pdl_sdbx_apikey_01jkdpbhazdpn3wpcya45as9tg_clientsecret_abc"


@fixture
def test_client(test_logger):
    # Rotation methods read the key ID from the client's API key
    return TestClient(api_secret_key=CLIENT_API_KEY, environment=Environment.SANDBOX, logger=test_logger)


class TestApiKeysClient:
    @mark.parametrize(
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                ListApiKeys(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/api-keys",
            ),
            (
                ListApiKeys(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/api-keys?order_by=id[asc]&per_page=50",
            ),
            (
                ListApiKeys(Pager(after="apikey_01jkdpbhazdpn3wpcya45as9tg")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/api-keys?after=apikey_01jkdpbhazdpn3wpcya45as9tg&order_by=id[asc]&per_page=50",
            ),
        ],
        ids=[
            "List API keys without pagination",
            "List API keys with default pagination",
            "List paginated API keys after specified API key id",
        ],
    )
    def test_list_api_keys_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.api_keys.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, ApiKeyCollection)
        assert all(isinstance(item, ApiKey) for item in response.items)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(PayloadEncoder().encode(response.items[0])) == loads(expected_response_body)["data"][0]
        assert loads(PayloadEncoder().encode(response.items[1])) == loads(expected_response_body)["data"][1]

    def test_list_api_keys_parses_nested_values(self, test_client, mock_requests):
        mock_requests.get(
            f"{test_client.base_url}/api-keys",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
        )

        response = test_client.client.api_keys.list()
        first, second = response.items

        assert first.id == "apikey_01jkdpbhazdpn3wpcya45as9tg"
        assert first.key == "pdl_live_apikey_01jkdpbhaz****"
        assert first.status == ApiKeyStatus.Active
        assert first.permissions == [
            ApiKeyPermission.AddressRead,
            ApiKeyPermission.BusinessRead,
            ApiKeyPermission.CustomerRead,
            ApiKeyPermission.SubscriptionRead,
            ApiKeyPermission.TransactionRead,
        ]
        assert first.exposed_at is None
        assert first.expires_at == datetime(2026, 3, 26, 6, 58, 38, 517000, tzinfo=timezone.utc)
        assert first.rotatable is True
        assert first.last_used_at == datetime(2025, 10, 20, 9, 12, 44, tzinfo=timezone.utc)

        assert second.status == ApiKeyStatus.Revoked
        assert ApiKeyPermission.ApiKeyRead in second.permissions
        assert second.description is None
        assert second.exposed_at == datetime(2025, 11, 1, 10, 0, 0, tzinfo=timezone.utc)
        assert second.expires_at is None
        assert second.last_used_at is None
        assert second.rotatable is False

    def test_list_api_keys_can_paginate(self, test_client, mock_requests):
        mock_requests.get(
            f"{test_client.base_url}/api-keys",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
        )
        mock_requests.get(
            f"{test_client.base_url}/api-keys?after=apikey_01jkdpcy050kbc638ekh5ps5hj&per_page=2",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_page_two"),
        )

        response = test_client.client.api_keys.list()

        assert isinstance(response, ApiKeyCollection)
        assert len([api_key for api_key in response]) == 3

    @mark.parametrize(
        "api_key_id, expected_response_status, expected_response_body, expected_url",
        [
            (
                "apikey_01jkdpbhazdpn3wpcya45as9tg",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg",
            ),
            (
                "apikey_01jkdpdy050kbc638ekh5ps5hk",
                200,
                ReadsFixtures.read_raw_json_fixture("response/legacy_entity"),
                "/api-keys/apikey_01jkdpdy050kbc638ekh5ps5hk",
            ),
        ],
        ids=["Get API key", "Get legacy API key with null permissions"],
    )
    def test_get_api_key_returns_expected_response(
        self,
        test_client,
        mock_requests,
        api_key_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.api_keys.get(api_key_id)
        response_json = test_client.client.api_keys.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, ApiKey)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body))
        assert loads(PayloadEncoder().encode(response)) == loads(expected_response_body)["data"]
        assert response.id == api_key_id

    def test_get_legacy_api_key_has_null_permissions(self, test_client, mock_requests):
        mock_requests.get(
            f"{test_client.base_url}/api-keys/apikey_01jkdpdy050kbc638ekh5ps5hk",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/legacy_entity"),
        )

        response = test_client.client.api_keys.get("apikey_01jkdpdy050kbc638ekh5ps5hk")

        assert response.permissions is None
        assert response.key == "a1b2c3****"

    @mark.parametrize(
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                ListApiKeyRotations(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_one"),
                "/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations",
            ),
            (
                ListApiKeyRotations(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_one"),
                "/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations?order_by=id[asc]&per_page=50",
            ),
            (
                ListApiKeyRotations(Pager(after="apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_one"),
                "/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations?after=apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7&order_by=id[asc]&per_page=50",
            ),
            (
                ListApiKeyRotations(ids=["apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_one"),
                "/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations?id=apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7",
            ),
            (
                ListApiKeyRotations(ids=["apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7", "apkrot_01kjnm4a3w4jqdbtqvb2jwjdf8"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_one"),
                "/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations?id=apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7,apkrot_01kjnm4a3w4jqdbtqvb2jwjdf8",
            ),
        ],
        ids=[
            "List API key rotations without pagination",
            "List API key rotations with default pagination",
            "List paginated API key rotations after specified rotation id",
            "List API key rotations filtered by a single id",
            "List API key rotations filtered by multiple ids",
        ],
    )
    def test_list_api_key_rotations_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.api_keys.list_current_key_rotations(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, ApiKeyRotationCollection)
        assert all(isinstance(item, ApiKeyRotation) for item in response.items)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(PayloadEncoder().encode(response.items[0])) == loads(expected_response_body)["data"][0]
        assert loads(PayloadEncoder().encode(response.items[1])) == loads(expected_response_body)["data"][1]

    def test_list_api_key_rotations_parses_nested_values(self, test_client, mock_requests):
        mock_requests.get(
            f"{test_client.base_url}/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_one"),
        )

        response = test_client.client.api_keys.list_current_key_rotations()
        completed, pending = response.items

        assert completed.status == ApiKeyRotationStatus.Completed
        assert completed.api_key_id == "apikey_01jkdpbhazdpn3wpcya45as9tg"
        assert completed.new_key == "pdl_live_apikey_01jkdpbhaz****"
        assert completed.grace_period_seconds == 3600
        assert completed.new_key_expires_at == datetime(2026, 11, 2, tzinfo=timezone.utc)
        assert completed.expires_at == datetime(2026, 10, 2, 10, 5, tzinfo=timezone.utc)

        assert pending.status == ApiKeyRotationStatus.Pending
        assert pending.grace_period_seconds == 0
        assert pending.new_key_expires_at is None
        assert pending.expires_at is None

    def test_list_api_key_rotations_can_paginate(self, test_client, mock_requests):
        base = f"{test_client.base_url}/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations"
        mock_requests.get(
            base,
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_one"),
        )
        mock_requests.get(
            f"{base}?after=apkrot_01kjnm4a3w4jqdbtqvb2jwjdf8&per_page=2",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_rotations_page_two"),
        )

        response = test_client.client.api_keys.list_current_key_rotations()

        assert isinstance(response, ApiKeyRotationCollection)
        rotations = [rotation for rotation in response]
        assert len(rotations) == 3
        assert rotations[2].status == ApiKeyRotationStatus.Canceled

    def test_get_api_key_rotation_returns_expected_response(self, test_client, mock_requests):
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/rotation_entity")
        expected_url = (
            f"{test_client.base_url}/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg"
            "/rotations/apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7"
        )
        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.api_keys.get_current_key_rotation("apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7")
        response_json = test_client.client.api_keys.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, ApiKeyRotation)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert response_json == loads(expected_response_body)
        assert loads(PayloadEncoder().encode(response)) == loads(expected_response_body)["data"]
        assert response.status == ApiKeyRotationStatus.Completed
        assert response.new_key == "pdl_live_apikey_01jkdpbhaz****"

    @mark.parametrize(
        "operation, expected_request_body, expected_response_body",
        [
            (
                CreateApiKeyRotation(
                    grace_period_seconds=3600,
                    new_key_expires_at=datetime(2026, 11, 2, tzinfo=timezone.utc),
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_rotation_full"),
                ReadsFixtures.read_raw_json_fixture("response/rotation_created_entity"),
            ),
            (
                CreateApiKeyRotation(
                    grace_period_seconds=3600,
                    new_key_expires_at=DateTime("2026-11-02T00:00:00.000000Z"),
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_rotation_full"),
                ReadsFixtures.read_raw_json_fixture("response/rotation_created_entity"),
            ),
            (
                CreateApiKeyRotation(grace_period_seconds=0),
                ReadsFixtures.read_raw_json_fixture("request/create_rotation_minimal"),
                ReadsFixtures.read_raw_json_fixture("response/rotation_created_minimal_entity"),
            ),
        ],
        ids=[
            "Create API key rotation with new key expiry as datetime",
            "Create API key rotation with new key expiry as DateTime",
            "Create API key rotation with grace period only",
        ],
    )
    def test_create_api_key_rotation_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_body,
    ):
        expected_url = f"{test_client.base_url}/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations"
        mock_requests.post(expected_url, status_code=201, text=expected_response_body)

        response = test_client.client.api_keys.rotate_current_key(operation)
        response_json = test_client.client.api_keys.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, ApiKeyRotationCreated)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == 201
        assert unquote(last_request.url) == expected_url
        assert loads(request_json) == loads(expected_request_body)
        assert response_json == loads(expected_response_body)
        assert loads(PayloadEncoder().encode(response)) == loads(expected_response_body)["data"]
        assert response.status == ApiKeyRotationStatus.Pending
        assert response.new_key == "pdl_live_apikey_01jkdpbhazdpn3wpcya45as9tg_somesecret_abc"
        assert response.expires_at is None

    def test_list_api_key_rotations_rejects_non_string_ids(self):
        with raises(InvalidArgumentException):
            ListApiKeyRotations(ids=[123])

    def test_create_api_key_rotation_keeps_new_key_out_of_logs_and_repr(
        self, test_client, mock_requests, test_logger, test_log_handler
    ):
        new_key = "pdl_live_apikey_01jkdpbhazdpn3wpcya45as9tg_somesecret_abc"
        previous_level = test_logger.level
        test_logger.setLevel(logging.DEBUG)
        mock_requests.post(
            f"{test_client.base_url}/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations",
            status_code=201,
            text=ReadsFixtures.read_raw_json_fixture("response/rotation_created_entity"),
        )

        try:
            response = test_client.client.api_keys.rotate_current_key(CreateApiKeyRotation(grace_period_seconds=3600))
        finally:
            test_logger.setLevel(previous_level)

        log_text = "\n".join(record.getMessage() for record in test_log_handler.get_logs())
        assert '"new_key": "[REDACTED]"' in log_text
        assert new_key not in log_text
        assert new_key not in repr(response)
        assert new_key not in str(response)
        assert response.new_key == new_key

    def test_current_key_rotations_authenticate_with_the_client_api_key(self, test_client, mock_requests):
        mock_requests.post(
            f"{test_client.base_url}/api-keys/apikey_01jkdpbhazdpn3wpcya45as9tg/rotations",
            status_code=201,
            text=ReadsFixtures.read_raw_json_fixture("response/rotation_created_entity"),
        )

        test_client.client.api_keys.rotate_current_key(CreateApiKeyRotation(grace_period_seconds=3600))

        assert mock_requests.last_request.headers["Authorization"] == f"Bearer {CLIENT_API_KEY}"

    @mark.parametrize(
        "call",
        [
            lambda api_keys: api_keys.rotate_current_key(CreateApiKeyRotation(grace_period_seconds=3600)),
            lambda api_keys: api_keys.list_current_key_rotations(),
            lambda api_keys: api_keys.get_current_key_rotation("apkrot_01kjnm4a3w4jqdbtqvb2jwjdf7"),
        ],
        ids=["Rotate", "List", "Get"],
    )
    def test_current_key_rotations_fail_when_the_client_api_key_cannot_be_rotated(
        self, test_logger, mock_requests, call
    ):
        client = TestClient(api_secret_key="API_KEY_PLACEHOLDER", logger=test_logger).client

        with raises(InvalidArgumentException):
            call(client.api_keys)

        assert mock_requests.call_count == 0
