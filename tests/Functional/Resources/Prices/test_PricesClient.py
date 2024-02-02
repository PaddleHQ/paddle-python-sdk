from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import PriceCollection
from paddle_billing.Entities.Price       import Price
from paddle_billing.Entities.Shared      import (
    CountryCode,
    CurrencyCode,
    CustomData,
    Interval,
    Money,
    PriceQuantity,
    Status,
    TaxMode,
    TimePeriod,
    UnitPriceOverride
)

from paddle_billing.Resources.Prices.Operations import CreatePrice, ListPrices, UpdatePrice, PriceIncludes
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestPricesClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                CreatePrice(
                    description = 'Monthly (per seat)',
                    product_id  = 'pro_01h7zcgmdc6tmwtjehp3sh7azf',
                    unit_price  = Money('500', CurrencyCode.USD),
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/prices',
            ), (
                CreatePrice(
                    description   = "Weekly (per seat)",
                    product_id    = "pro_01gsz4t5hdjse780zja8vvr7jg",
                    unit_price    = Money("1000", CurrencyCode.GBP),
                    name          = "Weekly",
                    tax_mode      = TaxMode.AccountSetting,
                    trial_period  = TimePeriod(Interval.Week, 1),
                    billing_cycle = TimePeriod(Interval.Year, 1),
                    quantity      = PriceQuantity(1, 1),
                    custom_data   = CustomData({"foo": "bar"}),

                    unit_price_overrides = [
                        UnitPriceOverride(
                            country_codes = [CountryCode.CA, CountryCode.US],
                            unit_price    = Money("5000", CurrencyCode.USD),
                        ),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/prices',
            ),
        ],
        ids=[
            "Create price with basic data",
            "Create price with full data",
        ],
    )
    def test_create_price_uses_expected_payload(
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

        response      = test_client.client.prices.create(operation)
        response_json = test_client.client.prices.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Price)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                UpdatePrice(name='Annually'),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/prices/pro_01h7zcgmdc6tmwtjehp3sh7azf',
            ), (
                UpdatePrice(name='Annually', unit_price=Money('100000', CurrencyCode.GBP)),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/prices/pro_01h7zcgmdc6tmwtjehp3sh7azf',
            ), (
                UpdatePrice(
                    name                 = 'Annually',
                    description          = 'Annually (per seat)',
                    unit_price           = Money('100000', CurrencyCode.GBP),
                    unit_price_overrides = [UnitPriceOverride([CountryCode.US], Money('200000', CurrencyCode.USD))],
                    quantity             = PriceQuantity(1, 10),
                    trial_period         = TimePeriod(Interval.Month, 1),
                    billing_cycle        = TimePeriod(Interval.Year, 1),
                    tax_mode             = TaxMode.External,
                    custom_data          = CustomData({'features': {'reports': True}}),
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/prices/pro_01h7zcgmdc6tmwtjehp3sh7azf'
            ),
        ],
        ids=[
            "Update price with single new value",
            "Update price with partial new values",
            "Update price with completely new values",
        ],
    )
    def test_update_price_uses_expected_payload(
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
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.prices.update('pro_01h7zcgmdc6tmwtjehp3sh7azf', operation)
        response_json = test_client.client.prices.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Price)
        assert last_request is not None
        assert last_request.method            == 'PATCH'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                ListPrices(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices',
            ), (
                ListPrices(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?order_by=id[asc]&per_page=50',
            ), (
                ListPrices(Pager(after='pro_01gsz4s0w61y0pp88528f1wvvb')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?after=pro_01gsz4s0w61y0pp88528f1wvvb&order_by=id[asc]&per_page=50',
            ), (
                ListPrices(statuses=[Status.Archived]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?status=archived',
            ), (
                ListPrices(ids=['pri_01gsz4s0w61y0pp88528f1wvvb']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?id=pri_01gsz4s0w61y0pp88528f1wvvb',
            ), (
                ListPrices(ids=['pri_01gsz4s0w61y0pp88528f1wvvb', 'pri_01h1vjes1y163xfj1rh1tkfb65']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?id=pri_01gsz4s0w61y0pp88528f1wvvb,pri_01h1vjes1y163xfj1rh1tkfb65',
            ), (
                ListPrices(product_ids=['pro_01gsz4s0w61y0pp88528f1wvvb']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?product_id=pro_01gsz4s0w61y0pp88528f1wvvb',
            ), (
                ListPrices(product_ids=['pro_01gsz4s0w61y0pp88528f1wvvb', 'pro_01h1vjes1y163xfj1rh1tkfb65']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?product_id=pro_01gsz4s0w61y0pp88528f1wvvb,pro_01h1vjes1y163xfj1rh1tkfb65',
            ), (
                ListPrices(recurring=True),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?recurring=true',
            ), (
                ListPrices(includes=[PriceIncludes.Product]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/prices?include=product',
            ),
        ],
        ids=[
            "List prices without pagination",
            "List prices with default pagination",
            "List paginated prices after specified product id",
            "List prices filtered by status",
            "List prices filtered by id",
            "List prices filtered by multiple ids",
            "List prices filtered by product id",
            "List prices filtered by multiple product ids",
            "List prices filtered by recurring prices",
            "List prices with includes",
        ],
    )
    def test_list_prices_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status)

        response     = test_client.client.prices.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, PriceCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'price_id, includes, expected_response_status, expected_response_body, expected_url',
        [
            (
                'pri_01h7zcgmdc6tmwtjehp3sh7azf',
                None,
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/prices/pri_01h7zcgmdc6tmwtjehp3sh7azf',
            ), (
                'pri_01h7zcgmdc6tmwtjehp3sh7azf',
                [PriceIncludes.Product],
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity_with_includes'),
                '/prices/pri_01h7zcgmdc6tmwtjehp3sh7azf?include=product',
            ),
        ],
        ids=[
            "Get price",
            "Get price with includes",
        ],
    )
    def test_get_prices_returns_expected_response(
        self,
        test_client,
        mock_requests,
        price_id,
        includes,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.prices.get(price_id, includes=includes)
        response_json = test_client.client.prices.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Price)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
