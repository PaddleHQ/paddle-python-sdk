from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import NotificationLogCollection

from paddle_billing.Resources.NotificationLogs.Operations import ListNotificationLogs
from paddle_billing.Resources.Shared.Operations           import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


# The notification id to use for these tests
TEST_ID = 'ntf_01hher6hqs35t9dzq84g3ggqvh'


class TestNotificationLogsClient:
    @mark.parametrize(
        'operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                ListNotificationLogs(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                f"/notifications/{TEST_ID}/logs"
            ), (
                ListNotificationLogs(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                f"/notifications/{TEST_ID}/logs?order_by=id[asc]&per_page=50"
            ), (
                ListNotificationLogs(Pager(after='pro_01gsz4s0w61y0pp88528f1wvvb')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                f"/notifications/{TEST_ID}/logs?after=pro_01gsz4s0w61y0pp88528f1wvvb&order_by=id[asc]&per_page=50"
            ),
        ],
        ids=[
            "List events",
            "List paginated events",
            "List paginated events after specified product id",
        ],
    )
    def test_list_notification_logs_returns_expected_response(
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

        response      = test_client.client.notification_logs.list(TEST_ID, operation=operation)
        response_json = test_client.client.notification_logs.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, NotificationLogCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"
