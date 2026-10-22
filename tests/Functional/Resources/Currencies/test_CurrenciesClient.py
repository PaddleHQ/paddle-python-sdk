from json import loads
from urllib.parse import unquote

from paddle_billing.Entities.Collections import CurrencyDefinitionCollection
from paddle_billing.Entities.Shared import CountryCode, CurrencyCode

from tests.Utils.ReadsFixture import ReadsFixtures


class TestCurrenciesClient:
    def test_list_currencies_returns_expected_response(self, test_client, mock_requests):
        expected_body = ReadsFixtures.read_raw_json_fixture("response/list_default")
        expected_url = f"{test_client.base_url}/currencies"
        mock_requests.get(expected_url, status_code=200, text=expected_body)

        currencies = test_client.client.currencies.list()
        response_json = test_client.client.currencies.response.json()
        last_request = mock_requests.last_request

        assert isinstance(currencies, CurrencyDefinitionCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert response_json == loads(str(expected_body))

        currencies = list(currencies)
        assert len(currencies) == 2

        gbp = currencies[0]
        assert gbp.code == CurrencyCode.GBP
        assert gbp.name == "Pound Sterling"
        assert gbp.decimal_places == 2
        assert gbp.can_be_balance is True
        assert gbp.applicable_countries[:2] == [CountryCode.FK, CountryCode.GB]
        assert len(gbp.applicable_countries) == 9
        assert gbp.minimum_payment_amount == "55"

        assert currencies[1].can_be_balance is False
