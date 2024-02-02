from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import DiscountCollection
from paddle_billing.Entities.Discount    import Discount
from paddle_billing.Entities.Discounts   import DiscountStatus, DiscountType
from paddle_billing.Entities.Shared      import CurrencyCode, Status

from paddle_billing.Resources.Discounts.Operations import CreateDiscount, ListDiscounts, UpdateDiscount
from paddle_billing.Resources.Shared.Operations    import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestDiscountsClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                CreateDiscount(
                    '10',
                    'Nonprofit discount',
                    DiscountType.Percentage,
                    True,
                    True,
                    CurrencyCode.USD,
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/discounts',
            ), (
                CreateDiscount(
                    '10',
                    'Nonprofit discount',
                    DiscountType.Percentage,
                    True,
                    True,
                    CurrencyCode.USD,
                    code='ABCDE12345',
                    maximum_recurring_intervals=5,
                    usage_limit=1000,
                    restrict_to=['pro_01gsz4t5hdjse780zja8vvr7jg', 'pro_01gsz4s0w61y0pp88528f1wvvb'],
                    expires_at='2025-01-01 10:00:00',
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/discounts',
            ),
        ],
        ids=[
            "Create discount with basic data",
            "Create discount with full data",
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

        response      = test_client.client.discounts.create(operation)
        response_json = test_client.client.discounts.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Discount)
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
        'discount_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'dsc_01h83xenpcfjyhkqr4x214m02x',
                UpdateDiscount(enabled_for_checkout=False),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/discounts/dsc_01h83xenpcfjyhkqr4x214m02x',
            ), (
                'dsc_01h83xenpcfjyhkqr4x214m02x',
                UpdateDiscount(enabled_for_checkout=False, code=None),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/discounts/dsc_01h83xenpcfjyhkqr4x214m02x',
            ), (
                'dsc_01h83xenpcfjyhkqr4x214m02x',
                UpdateDiscount(
                    description                 = 'Nonprofit discount',
                    enabled_for_checkout        = True,
                    type                        = DiscountType.Percentage,
                    amount                      = '10',
                    recur                       = True,
                    currency_code               = CurrencyCode.USD,
                    code                        = 'ABCDE12345',
                    maximum_recurring_intervals = 5,
                    usage_limit                 = 1000,
                    expires_at                  = '2025-01-01 10:00:00',
                    status                      = DiscountStatus.Active,
                    restrict_to                 = [
                        'pro_01gsz4t5hdjse780zja8vvr7jg',
                        'pro_01gsz4s0w61y0pp88528f1wvvb',
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/discounts/dsc_01h83xenpcfjyhkqr4x214m02x'
            ),
        ],
        ids=[
            "Update discount with single new value",
            "Update discount with partial new values",
            "Update discount with completely new values",
        ],
    )
    def test_update_discount_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        discount_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.discounts.update(discount_id, operation)
        response_json = test_client.client.discounts.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Discount)
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
                ListDiscounts(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts',
            ), (
                ListDiscounts(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts?order_by=id[asc]&per_page=50',
            ), (
                ListDiscounts(Pager(after='dsc_01h83xenpcfjyhkqr4x214m02x')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts?after=dsc_01h83xenpcfjyhkqr4x214m02x&order_by=id[asc]&per_page=50',
            ), (
                ListDiscounts(statuses=[Status.Archived]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts?status=archived',
            ), (
                ListDiscounts(ids=['dsc_01h83xenpcfjyhkqr4x214m02x']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts?id=dsc_01h83xenpcfjyhkqr4x214m02x',
            ), (
                ListDiscounts(ids=['dsc_01h83xenpcfjyhkqr4x214m02x', 'dsc_01gtgraak4chyhnp47rrdv89ad']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts?id=dsc_01h83xenpcfjyhkqr4x214m02x,dsc_01gtgraak4chyhnp47rrdv89ad',
            ), (
                ListDiscounts(codes=['ABCDE12345']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts?code=ABCDE12345',
            ), (
                ListDiscounts(codes=['ABCDE12345', '54321EDCBA']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/discounts?code=ABCDE12345,54321EDCBA',
            ),
        ],
        ids=[
            "List discounts without pagination",
            "List discounts with default pagination",
            "List paginated discounts after specified discount id",
            "List discounts filtered by archived status",
            "List discounts filtered by id",
            "List discounts filtered by multiple ids",
            "List discounts filtered by discount id",
            "List discounts filtered by multiple discount ids",
        ],
    )
    def test_list_discounts_returns_expected_response(
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

        response     = test_client.client.discounts.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, DiscountCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'discount_id, expected_response_status, expected_response_body, expected_url',
        [(
            'dsc_01h83xenpcfjyhkqr4x214m02x',
            200,
            ReadsFixtures.read_raw_json_fixture('response/full_entity'),
            '/discounts/dsc_01h83xenpcfjyhkqr4x214m02x',
        )],
        ids=["Get discount"],
    )
    def test_get_discounts_returns_expected_response(
        self,
        test_client,
        mock_requests,
        discount_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.discounts.get(discount_id)
        response_json = test_client.client.discounts.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Discount)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
