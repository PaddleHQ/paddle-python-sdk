from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import NotificationCollection
from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Notification import Notification
from paddle_billing.Entities.Notifications import NotificationEvent, NotificationStatus

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Adjustment import Adjustment
from paddle_billing.Notifications.Entities.Adjustments.AdjustmentTaxRatesUsed import AdjustmentTaxRatesUsed
from paddle_billing.Notifications.Entities.Business import Business

from paddle_billing.Resources.Notifications.Operations import ListNotifications
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


class TestNotificationsClient:
    @mark.parametrize(
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                ListNotifications(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications",
            ),
            (
                ListNotifications(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?order_by=id[asc]&per_page=50",
            ),
            (
                ListNotifications(Pager(after="nft_01h83xenpcfjyhkqr4x214m02x")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?after=nft_01h83xenpcfjyhkqr4x214m02x&order_by=id[asc]&per_page=50",
            ),
            (
                ListNotifications(notification_setting_ids=["nftset_01h83xenpcfjyhkqr4x214m02"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?notification_setting_id=nftset_01h83xenpcfjyhkqr4x214m02",
            ),
            (
                ListNotifications(
                    notification_setting_ids=[
                        "nftset_01h83xenpcfjyhkqr4x214m02",
                        "nftset_01h8brhckjd6qk4n7e4py2340t",
                    ]
                ),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?notification_setting_id=nftset_01h83xenpcfjyhkqr4x214m02,nftset_01h8brhckjd6qk4n7e4py2340t",
            ),
            (
                ListNotifications(statuses=[NotificationStatus.Delivered]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?status=delivered",
            ),
            (
                ListNotifications(statuses=[NotificationStatus.Delivered, NotificationStatus.NotAttempted]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?status=delivered,not_attempted",
            ),
            (
                ListNotifications(filter="txn_01h83xenpcfjyhkqr4x214m02"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?filter=txn_01h83xenpcfjyhkqr4x214m02",
            ),
            (
                ListNotifications(search="transaction.created"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?search=transaction.created",
            ),
            (
                ListNotifications(end=DateTime("2023-12-25T00:00:00.000Z")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?to=2023-12-25T00:00:00.000000Z",
            ),
            (
                ListNotifications(start=DateTime("2023-12-24T00:00:00.000Z")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?from=2023-12-24T00:00:00.000000Z",
            ),
            (
                ListNotifications(
                    start=DateTime("2023-12-24T00:00:00.000Z"),
                    end=DateTime("2023-12-25T00:00:00.000Z"),
                ),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/notifications?to=2023-12-25T00:00:00.000000Z&from=2023-12-24T00:00:00.000000Z",
            ),
        ],
        ids=[
            "List notifications without pagination",
            "List notifications with default pagination",
            "List paginated notifications after specified notification_id",
            "List notifications filtered by notification_setting_id",
            "List notifications filtered by multiple notification_setting_ids",
            "List notifications filtered by status",
            "List notifications filtered by multiple statuses",
            "List notifications filtered by id",
            "List notifications filtered by search string",
            "List notifications filtered by to time",
            "List notifications filtered by from time",
            "List notifications filtered by to & from time",
        ],
    )
    def test_list_notifications_returns_expected_response(
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

        response = test_client.client.notifications.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, NotificationCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

        assert len(response.items) == 7
        for notification in response.items:
            assert isinstance(notification, Notification)
            assert isinstance(notification.payload, NotificationEvent)
            assert notification.payload.notification_id is not None
            assert isinstance(notification.payload.data, Entity)

    def test_list_subscription_notification_with_and_without_product(
        self,
        test_client,
        mock_requests,
    ):
        expected_url = f"{test_client.base_url}/notifications"
        mock_requests.get(
            expected_url, status_code=200, text=ReadsFixtures.read_raw_json_fixture("response/list_default")
        )

        response = test_client.client.notifications.list(ListNotifications())
        subscription = response.items[3].payload.data

        itemWithoutProduct = subscription.items[0]
        assert itemWithoutProduct.product is None

        itemWithProduct = subscription.items[1]
        assert itemWithProduct.product is not None
        assert itemWithProduct.product.id == "pro_01h84cd36f900f3wmpdfamgv8w"

    def test_list_adjustment_notification_with_and_without_tax_rates_used(
        self,
        test_client,
        mock_requests,
    ):
        expected_url = f"{test_client.base_url}/notifications"
        mock_requests.get(
            expected_url, status_code=200, text=ReadsFixtures.read_raw_json_fixture("response/list_default")
        )

        response = test_client.client.notifications.list(ListNotifications())

        adjustmentWithTaxRatesUsed = response.items[5].payload.data
        assert isinstance(adjustmentWithTaxRatesUsed, Adjustment)

        tax_rates_used = adjustmentWithTaxRatesUsed.tax_rates_used[0]

        assert isinstance(tax_rates_used, AdjustmentTaxRatesUsed)
        assert tax_rates_used.tax_rate == "0.2"
        assert tax_rates_used.totals.total == "66000"
        assert tax_rates_used.totals.subtotal == "55000"
        assert tax_rates_used.totals.tax == "11000"

        adjustmentWithoutTaxRatesUsed = response.items[6].payload.data
        assert isinstance(adjustmentWithoutTaxRatesUsed, Adjustment)
        assert adjustmentWithoutTaxRatesUsed.tax_rates_used is None

    @mark.parametrize(
        "notification_id, expected_response_status, expected_response_body, expected_url",
        [
            (
                "nft_01h8441jn5pcwrfhwh78jqt8hk",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/notifications/nft_01h8441jn5pcwrfhwh78jqt8hk",
            )
        ],
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

        response = test_client.client.notifications.get(notification_id)
        response_json = test_client.client.notifications.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, Notification)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

        notification_event = response.payload
        assert isinstance(notification_event, NotificationEvent)
        assert notification_event.notification_id == "ntf_01h8bzam1z32agrxjwhjgqk8w6"
        assert notification_event.event_id == "evt_01h8bzakzx3hm2fmen703n5q45"
        assert notification_event.event_type == EventTypeName.BusinessUpdated
        assert notification_event.occurred_at.strftime("%Y-%m-%dT%H:%M:%S.%f") == "2023-08-21T11:57:47.390028"

        notification_entity = notification_event.data
        assert isinstance(notification_entity, Business)
        assert notification_entity.id == "biz_01h84a7hr4pzhsajkm8tev89ev"
        assert notification_entity.name == "ChatApp Inc."

    @mark.parametrize(
        "notification_id,"
        "expected_response_status,"
        "expected_response_body,"
        "expected_response_notification_id,"
        "expected_url",
        [
            (
                "nft_01h8441jn5pcwrfhwh78jqt8hk",
                200,
                ReadsFixtures.read_raw_json_fixture("response/replay"),
                "ntf_01h46h1s2zabpkdks7yt4vkgkc",
                "/notifications/nft_01h8441jn5pcwrfhwh78jqt8hk",
            )
        ],
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

        response = test_client.client.notifications.replay(notification_id)
        response_json = test_client.client.notifications.response.json()
        last_request = mock_requests.last_request

        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
        assert (
            response == expected_response_notification_id
        ), "The response notification_id doesn't match the expected fixture JSON notification_id"
