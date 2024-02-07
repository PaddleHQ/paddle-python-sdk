from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections   import NotificationCollection
from paddle_billing.Entities.DateTime      import DateTime
from paddle_billing.Entities.Notification  import Notification
from paddle_billing.Entities.Notifications import NotificationStatus

from paddle_billing.Resources.Notifications.Operations import ListNotifications
from paddle_billing.Resources.Shared.Operations        import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestNotificationsClient:
    @mark.parametrize(
        'operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                ListNotifications(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications',
            ), (
                ListNotifications(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?order_by=id[asc]&per_page=50',
            ), (
                ListNotifications(Pager(after='nft_01h83xenpcfjyhkqr4x214m02x')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?after=nft_01h83xenpcfjyhkqr4x214m02x&order_by=id[asc]&per_page=50',
            ), (
                ListNotifications(notification_setting_ids=['nftset_01h83xenpcfjyhkqr4x214m02']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?notification_setting_id=nftset_01h83xenpcfjyhkqr4x214m02',
            ), (
                ListNotifications(notification_setting_ids=[
                    'nftset_01h83xenpcfjyhkqr4x214m02',
                    'nftset_01h8brhckjd6qk4n7e4py2340t',
                ]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?notification_setting_id=nftset_01h83xenpcfjyhkqr4x214m02,nftset_01h8brhckjd6qk4n7e4py2340t',
            ), (
                ListNotifications(statuses=[NotificationStatus.Delivered]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?status=delivered',
            ), (
                ListNotifications(statuses=[NotificationStatus.Delivered, NotificationStatus.NotAttempted]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?status=delivered,not_attempted',
            ), (
                ListNotifications(filter='txn_01h83xenpcfjyhkqr4x214m02'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?filter=txn_01h83xenpcfjyhkqr4x214m02',
            ), (
                ListNotifications(search='transaction.created'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?search=transaction.created',
            ), (
                ListNotifications(end=DateTime('2023-12-25T00:00:00.000Z')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?to=2023-12-25T00:00:00.000000Z',
            ), (
                ListNotifications(start=DateTime('2023-12-24T00:00:00.000Z')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?from=2023-12-24T00:00:00.000000Z',
            ), (
                ListNotifications(
                    start = DateTime('2023-12-24T00:00:00.000Z'),
                    end   = DateTime('2023-12-25T00:00:00.000Z'),
                ),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/notifications?to=2023-12-25T00:00:00.000000Z&from=2023-12-24T00:00:00.000000Z',
            ),
        ],
        ids=[
            "List transactions without pagination",
            "List transactions with default pagination",
            "List paginated transactions after specified transaction_id",
            "List transactions filtered by notification_setting_id",
            "List transactions filtered by multiple notification_setting_ids",
            "List transactions filtered by status",
            "List transactions filtered by multiple statuses",
            "List transactions filtered by id",
            "List transactions filtered by search string",
            "List transactions filtered by to time",
            "List transactions filtered by from time",
            "List transactions filtered by to & from time",
        ],
    )
    def test_list_transactions_returns_expected_response(
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

        response     = test_client.client.notifications.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, NotificationCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"

    @mark.parametrize(
        'notification_id, expected_response_status, expected_response_body, expected_url',
        [(
            'nft_01h8441jn5pcwrfhwh78jqt8hk',
            200,
            ReadsFixtures.read_raw_json_fixture('response/full_entity'),
            '/notifications/nft_01h8441jn5pcwrfhwh78jqt8hk',
        )],
        ids=["Get a notification by its id"],
    )
    def test_get_notification_returns_expected_response(
        self,
        test_client,
        mock_requests,
        notification_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.notifications.get(notification_id)
        response_json = test_client.client.notifications.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Notification)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"


    @mark.parametrize(
        'notification_id,'
        'expected_response_status,'
        'expected_response_body,'
        'expected_response_notification_id,'
        'expected_url',
        [(
            'nft_01h8441jn5pcwrfhwh78jqt8hk',
            200,
            ReadsFixtures.read_raw_json_fixture('response/replay'),
            'ntf_01h46h1s2zabpkdks7yt4vkgkc',
            '/notifications/nft_01h8441jn5pcwrfhwh78jqt8hk',
        )],
        ids=["Replay a notification by its id"],
    )
    def test_replacy_notification_returns_expected_response(
        self,
        test_client,
        mock_requests,
        notification_id,
        expected_response_status,
        expected_response_body,
        expected_response_notification_id,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.notifications.replay(notification_id)
        response_json = test_client.client.notifications.response.json()
        last_request  = mock_requests.last_request

        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
        assert response == expected_response_notification_id, \
            "The response notification_id doesn't match the expected fixture JSON notification_id"
