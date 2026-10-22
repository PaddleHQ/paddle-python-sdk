from json import loads
from urllib.parse import unquote

from paddle_billing.Entities.Collections import CountryDefinitionCollection
from paddle_billing.Entities.Countries import CountryDefinitionTaxMode
from paddle_billing.Entities.Shared import CountryCode, CountryCodeIso3, CurrencyCode, CurrencyCodePayouts

from tests.Utils.ReadsFixture import ReadsFixtures


class TestCountriesClient:
    def test_list_countries_returns_expected_response(self, test_client, mock_requests):
        expected_body = ReadsFixtures.read_raw_json_fixture("response/list_default")
        expected_url = f"{test_client.base_url}/countries"
        mock_requests.get(expected_url, status_code=200, text=expected_body)

        countries = test_client.client.countries.list()
        response_json = test_client.client.countries.response.json()
        last_request = mock_requests.last_request

        assert isinstance(countries, CountryDefinitionCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert response_json == loads(str(expected_body))

        countries = list(countries)
        assert len(countries) == 3

        us = countries[0]
        assert us.iso == CountryCode.US
        assert us.iso3 == CountryCodeIso3.USA
        assert us.name == "UNITED STATES"
        assert us.printable_name == "United States"
        assert us.uses_postal_code is True
        assert us.transaction_currency == CurrencyCode.USD
        assert us.payout_currency == CurrencyCodePayouts.USD
        assert us.allow_sales is True
        assert us.has_regions is False
        assert us.tax_mode == CountryDefinitionTaxMode.External

        assert countries[1].tax_mode == CountryDefinitionTaxMode.Internal

    def test_list_countries_parses_non_supported_country(self, test_client, mock_requests):
        mock_requests.get(
            f"{test_client.base_url}/countries",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_default"),
        )

        russia = list(test_client.client.countries.list())[2]

        assert russia.iso3 == CountryCodeIso3.RUS
        assert russia.allow_sales is False
        assert russia.has_regions is True
