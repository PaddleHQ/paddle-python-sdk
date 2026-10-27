from json import loads
from urllib.parse import unquote

from paddle_billing.Entities.ApiRoot import RootApi, RootAuthType, RootCaller, RootCallerAccount, RootEnvironment
from paddle_billing.Entities.RootContext import RootContext

from tests.Utils.ReadsFixture import ReadsFixtures


class TestAPIRootClient:
    def test_get_api_root_returns_authenticated_response(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/authenticated")
        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.api_root.get()
        response_json = test_client.client.api_root.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, RootContext)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert response_json == loads(expected_response_body)
        assert isinstance(response.api, RootApi)
        assert response.api.name == "Paddle API"
        assert response.api.version == "1"
        assert response.api.environment == RootEnvironment.Production
        assert response.api.documentation_url == "https://developer.paddle.com/api-reference/overview"
        assert isinstance(response.caller, RootCaller)
        assert response.caller.auth_type == RootAuthType.ApiKey
        assert isinstance(response.caller.account, RootCallerAccount)
        assert response.caller.account.id == "slr_01k1e8w9df9pz73s399svdkxtg"
        assert response.caller.account.name == "AeroEdit"
        assert response.caller.permissions == [
            "transaction.read",
            "transaction.write",
            "subscription.read",
            "customer.read",
        ]

    def test_get_api_root_returns_unauthenticated_response(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/"
        mock_requests.get(
            expected_url, status_code=200, text=ReadsFixtures.read_raw_json_fixture("response/unauthenticated")
        )

        response = test_client.client.api_root.get()

        assert isinstance(response, RootContext)
        assert response.api.environment == RootEnvironment.Production
        assert response.caller.auth_type is None
        assert response.caller.account is None
        assert response.caller.permissions == []
