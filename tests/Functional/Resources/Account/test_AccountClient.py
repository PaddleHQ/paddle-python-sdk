from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.AccountDetails import AccountDetails
from paddle_billing.Resources.Account.Operations import UpdateAccount

from tests.Utils.ReadsFixture import ReadsFixtures


class TestAccountClient:
    def test_get_account_returns_expected_response(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/account"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")
        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.account.get()
        response_json = test_client.client.account.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, AccountDetails)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert response_json == loads(expected_response_body)
        assert response.id == "slr_01k1e8w9df9pz73s399svdkxtg"
        assert response.legacy_id == "15839"
        assert response.legal_name == "AeroEdit Inc."
        assert response.display_name == "AeroEdit"
        assert response.website == "https://example.com"
        assert response.email == "hello@example.com"

    def test_get_account_handles_null_fields(self, test_client, mock_requests):
        expected_url = f"{test_client.base_url}/account"
        mock_requests.get(
            expected_url,
            status_code=200,
            text=(
                '{"data": {"id": "slr_01k1e8w9df9pz73s399svdkxtg", "legacy_id": null, "legal_name": null, '
                '"display_name": null, "website": null, "email": null}, "meta": {"request_id": "abc"}}'
            ),
        )

        response = test_client.client.account.get()

        assert response.id == "slr_01k1e8w9df9pz73s399svdkxtg"
        assert response.legacy_id is None
        assert response.legal_name is None
        assert response.display_name is None
        assert response.website is None
        assert response.email is None

    @mark.parametrize(
        "operation, expected_request_body",
        [
            (UpdateAccount(email="billing@example.com"), ReadsFixtures.read_raw_json_fixture("request/update_email")),
            (UpdateAccount(), "{}"),
        ],
        ids=["Update account email", "Update account with no fields sends empty body"],
    )
    def test_update_account_uses_expected_payload(self, test_client, mock_requests, operation, expected_request_body):
        expected_url = f"{test_client.base_url}/account"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/updated_entity")
        mock_requests.patch(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.account.update(operation)
        response_json = test_client.client.account.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, AccountDetails)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert loads(request_json) == loads(expected_request_body)
        assert response_json == loads(expected_response_body)
        assert response.email == "billing@example.com"
