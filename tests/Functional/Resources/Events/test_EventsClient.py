from pytest       import mark
from urllib.parse import unquote

from paddle_billing_python_sdk.Environment import Environment

from paddle_billing_python_sdk.Entities.Collections.EventCollection   import EventCollection
from paddle_billing_python_sdk.Resources.Events.Operations.ListEvents import ListEvents
from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager

from tests.Utils.TestClient   import setup_test_client, mock_requests
from tests.Utils.ReadsFixture import ReadsFixtures


class TestEventsClient:
    @mark.parametrize(
        'operation, expected_status, expected_body, expected_uri',
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
    def test_list_hits_expected_uri(self, setup_test_client, mock_requests, operation, expected_status, expected_body, expected_uri):
        # Set up mock response
        mock_requests.get(expected_uri, status_code=expected_status, text=expected_body)

        print(f"operation={operation}")
        print(f"operation.get_parameters()={operation.get_parameters()}")
        print(f"dir(operation)={dir(operation)}")

        response = None
        try:
            response = setup_test_client.client.events.list(operation)
        except Exception as error:
            print(f"response error: {error}")

        last_request = mock_requests.last_request

        assert isinstance(response, EventCollection)
        assert last_request is not None
        assert last_request.method       == 'GET'
        assert unquote(last_request.url) == expected_uri
