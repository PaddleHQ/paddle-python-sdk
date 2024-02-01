from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import EventTypeCollection

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestEventTypesClient:
    @mark.parametrize(
        'expected_response_status, expected_response_body, expected_url',
        [(
            200,
            ReadsFixtures.read_raw_json_fixture('response/list_default'),
            '/event-types',
        )],
        ids=["List event types"],
    )
    def test_list_event_types_returns_expected_response(
        self,
        test_client,
        mock_requests,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        event_types   = test_client.client.event_types.list()
        response_json = test_client.client.event_types.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(event_types, EventTypeCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"
