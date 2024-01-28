import pytest
from json import loads as json_loads

from paddle_billing_python_sdk.Environment import Environment

from paddle_billing_python_sdk.Entities.Collections.EventCollection   import EventCollection
from paddle_billing_python_sdk.Resources.Events.Operations.ListEvents import ListEvents
from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager

from tests.Utils.TestClient   import setup_test_client, mock_requests
from tests.Utils.ReadsFixture import ReadsFixtures


class TestEventsClient:
    @pytest.mark.parametrize(
        'operation, expected_status, expected_body, expected_uri',
        [
            (
                ListEvents(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                f"{Environment.SANDBOX.base_url}/events"
            ), (
                ListEvents(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                # f"{Environment.SANDBOX.base_url}/events?order_by=id[asc]&per_page=50"
                f"{Environment.SANDBOX.base_url}/events"
            ), (
                ListEvents(Pager(after='evt_01h83xenpcfjyhkqr4x214m02x')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                # f"{Environment.SANDBOX.base_url}/events?after=evt_01h83xenpcfjyhkqr4x214m02x&order_by=id[asc]&per_page=50"
                f"{Environment.SANDBOX.base_url}/events"
            ),
        ]
    )
    def test_list_hits_expected_uri(self, setup_test_client, mock_requests, operation, expected_status, expected_body, expected_uri):
        # Set up mock response
        mock_requests.get(expected_uri, status_code=expected_status, text=expected_body)

        # Perform the operation
        try:
            response = setup_test_client.client.events.list(operation)
            print(f"response: {response}")
            print(dir(response))
        except Exception as error:
            print(f"response error: {error}")


        print()

        # Assertions
        last_request = mock_requests.last_request
        print(f"dir(last_request) ={dir(last_request)}")
        print(f"last_request.qs   ={last_request.qs}")
        print(f"last_request.query={last_request.query}")
        print(f"last_request.url  ={last_request.url}")
        print(f"expected_uri      ={expected_uri}")

        assert isinstance(response, EventCollection)
        assert last_request is not None
        assert last_request.method == 'GET'
        assert last_request.url == expected_uri
        # assert last_request.text == expected_body  # not needed
