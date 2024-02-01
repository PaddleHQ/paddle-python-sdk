from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.PricePreview    import PricePreview
from paddle_billing.Entities.PricingPreviews import PricePreviewItem
from paddle_billing.Entities.Shared          import AddressPreview, CountryCode, CurrencyCode

from paddle_billing.Resources.PricingPreviews.Operations import PreviewPrice

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestPricingPreviewsClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                PreviewPrice([PricePreviewItem('pri_01gsz8z1q1n00f12qt82y31smh', 20)]),
                ReadsFixtures.read_raw_json_fixture('request/preview_prices_minimal'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/pricing-preview',
            ), (
                PreviewPrice(
                    [
                        PricePreviewItem('pri_01gsz8z1q1n00f12qt82y31smh', 20),
                        PricePreviewItem('pri_01gsz98e27ak2tyhexptwc58yk', 1),
                    ],
                    currency_code       = CurrencyCode.USD,
                    discount_id         = 'dsc_01gtgztp8fpchantd5g1wrksa3',
                    customer_ip_address = '34.232.58.13',
                ),
                ReadsFixtures.read_raw_json_fixture('request/preview_prices_multiple'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/pricing-preview',
            ), (
                PreviewPrice(
                    [
                        PricePreviewItem('pri_01gsz8z1q1n00f12qt82y31smh', 20),
                        PricePreviewItem('pri_01gsz98e27ak2tyhexptwc58yk', 1),
                    ],
                    customer_id         = 'ctm_01h25m0sar5845yv5j8zj5xwe1',
                    address_id          = 'add_01h848pep46enq8y372x7maj0p',
                    business_id         = 'biz_01hfvpm3fj1my86qqs1c32mzsp',
                    currency_code       = CurrencyCode.USD,
                    discount_id         = 'dsc_01gtgztp8fpchantd5g1wrksa3',
                    address             = AddressPreview('20149', CountryCode.US),
                    customer_ip_address = '34.232.58.13',
                ),
                ReadsFixtures.read_raw_json_fixture('request/preview_prices_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/pricing-preview',
            ),
        ],
        ids=[
            "Preview a single price",
            "Preview multiple prices",
            "Preview multiple prices with full data",
        ],
    )
    def test_create_discount_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.pricing_previews.preview_prices(operation)
        response_json = test_client.client.pricing_previews.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, PricePreview)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"
