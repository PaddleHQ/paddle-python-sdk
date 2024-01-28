from pytest       import mark
from urllib.parse import unquote

from paddle_billing_python_sdk.Environment import Environment

from paddle_billing_python_sdk.Entities.Collections.EventCollection   import EventCollection
from paddle_billing_python_sdk.Resources.Events.Operations.ListEvents import ListEvents
from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestEventsClient:
    @mark.parametrize(
        'operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                ListEvents(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                f"{Environment.SANDBOX.base_url}/events",
            ), (
                ListEvents(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                f"{Environment.SANDBOX.base_url}/events?order_by=id[asc]&per_page=50",
            ), (
                ListEvents(Pager(after='evt_01h83xenpcfjyhkqr4x214m02x')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                f"{Environment.SANDBOX.base_url}/events?after=evt_01h83xenpcfjyhkqr4x214m02x&order_by=id[asc]&per_page=50",
            ),
        ],
        ids = [
            "List events",
            "List paginated events",
            "List paginated events after specified event id",
        ],
    )
    def test_list_hits_expected_url(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url
    ):
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response     = test_client.client.events.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, EventCollection)
        assert last_request is not None
        assert last_request.method       == 'GET'
        assert unquote(last_request.url) == expected_url, \
            "The URL does not match the expected URL, verify the Pagination query string is correct"
