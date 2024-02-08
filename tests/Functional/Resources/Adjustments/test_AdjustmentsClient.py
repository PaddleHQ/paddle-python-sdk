from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Adjustment  import Adjustment
from paddle_billing.Entities.Collections import AdjustmentCollection
from paddle_billing.Entities.Shared      import Action, AdjustmentStatus, AdjustmentType

from paddle_billing.Resources.Adjustments.Operations import CreateAdjustment, CreateAdjustmentItem, ListAdjustments
from paddle_billing.Resources.Shared.Operations      import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestAdjustmentsClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                CreateAdjustment(
                    Action.Refund,
                    [CreateAdjustmentItem('txnitm_01h8bxryv3065dyh6103p3yg28', AdjustmentType.Partial, '100')],
                    'error',
                    'txn_01h8bxpvx398a7zbawb77y0kp5',
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/adjustments',
            ), (
                CreateAdjustment(
                    Action.Refund,
                    [
                        CreateAdjustmentItem('txnitm_01h8bxryv3065dyh6103p3yg28', AdjustmentType.Partial, '100'),
                        CreateAdjustmentItem('txnitm_01h8bxryv3065dyh6103p3yg29', AdjustmentType.Full,    '1949'),
                    ],
                    'error',
                    'txn_01h8bxpvx398a7zbawb77y0kp5',
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/adjustments',
            ),
        ],
        ids=[
            "Create adjustment with basic data",
            "Create adjustment with full data",
        ],
    )
    def test_create_adjustment_uses_expected_payload(
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

        response      = test_client.client.adjustments.create(operation)
        response_json = test_client.client.adjustments.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Adjustment)
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
        'operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                ListAdjustments(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments',
            ), (
                ListAdjustments(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?order_by=id[asc]&per_page=50',
            ), (
                ListAdjustments(Pager(after='adj_01h8c65c2ggq5nxswnnwv78e75')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?after=adj_01h8c65c2ggq5nxswnnwv78e75&order_by=id[asc]&per_page=50',
            ), (
                ListAdjustments(statuses=[AdjustmentStatus.PendingApproval]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?status=pending_approval',
            ), (
                ListAdjustments(ids=['adj_01h8c65c2ggq5nxswnnwv78e75']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?id=adj_01h8c65c2ggq5nxswnnwv78e75',
            ), (
                ListAdjustments(ids=['add_01h8494f4w5rwfp8b12yqh8fp1', 'adj_01h8c65c2ggq5nxswnnwv78e75']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?id=add_01h8494f4w5rwfp8b12yqh8fp1,adj_01h8c65c2ggq5nxswnnwv78e75',
            ), (
                ListAdjustments(customer_ids=['ctm_01h8441jn5pcwrfhwh78jqt8hk']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?customer_id=ctm_01h8441jn5pcwrfhwh78jqt8hk',
            ), (
                ListAdjustments(customer_ids=['ctm_01h8441jn5pcwrfhwh78jqt8hk', 'ctm_01h7hswb86rtps5ggbq7ybydcw']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?customer_id=ctm_01h8441jn5pcwrfhwh78jqt8hk,ctm_01h7hswb86rtps5ggbq7ybydcw',
            ), (
                ListAdjustments(transaction_ids=['txn_01h8bxpvx398a7zbawb77y0kp5']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?transaction_id=txn_01h8bxpvx398a7zbawb77y0kp5',
            ), (
                ListAdjustments(transaction_ids=['ctm_01h8441jn5pcwrfhwh78jqt8hk', 'txn_01h8bx69629a16wwm9z8rjmak3']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?transaction_id=ctm_01h8441jn5pcwrfhwh78jqt8hk,txn_01h8bx69629a16wwm9z8rjmak3',
            ), (
                ListAdjustments(subscription_ids=['sub_01h8bxswamxysj44zt5n48njwh']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?subscription_id=sub_01h8bxswamxysj44zt5n48njwh',
            ), (
                ListAdjustments(subscription_ids=['sub_01h8bxswamxysj44zt5n48njwh', 'sub_01h8bx8fmywym11t6swgzba704']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?subscription_id=sub_01h8bxswamxysj44zt5n48njwh,sub_01h8bx8fmywym11t6swgzba704',
            ), (
                ListAdjustments(action=Action.Refund),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/adjustments?action=refund',
            ),
        ],
        ids=[
            "List adjustments without pagination",
            "List adjustments with default pagination",
            "List paginated adjustments after specified adjustment id",
            "List adjustments filtered by notification status",
            "List adjustments filtered by id",
            "List adjustments filtered by multiple ids",
            "List adjustments filtered by customer id",
            "List adjustments filtered by multiple customer ids",
            "List adjustments filtered by transaction id",
            "List adjustments filtered by multiple transaction ids",
            "List adjustments filtered by subscription id",
            "List adjustments filtered by multiple subscription ids",
            "List adjustments filtered by action",
        ],
    )
    def test_list_adjustments_returns_expected_response(
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

        response     = test_client.client.adjustments.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, AdjustmentCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
