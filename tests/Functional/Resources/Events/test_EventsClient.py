from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import EventCollection

from paddle_billing.Resources.Events.Operations import ListEvents
from paddle_billing.Resources.Shared.Operations import Pager

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
                '/events',
            ), (
                ListEvents(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/events?order_by=id[asc]&per_page=50',
            ), (
                ListEvents(Pager(after='evt_01h83xenpcfjyhkqr4x214m02x')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/events?after=evt_01h83xenpcfjyhkqr4x214m02x&order_by=id[asc]&per_page=50',
            ),
        ],
        ids=[
            "List events",
            "List paginated events",
            "List paginated events after specified event id",
        ],
    )
    def test_list_events_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        events        = test_client.client.events.list(operation)
        response_json = test_client.client.events.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(events, EventCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"
