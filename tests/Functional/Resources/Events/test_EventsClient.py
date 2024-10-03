from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import EventCollection
from paddle_billing.Entities.Event import Event

from paddle_billing.Resources.Events.Operations import ListEvents
from paddle_billing.Resources.Shared.Operations import Pager

from paddle_billing.Notifications.Entities.Subscription import Subscription
from paddle_billing.Notifications.Entities.SubscriptionCreated import SubscriptionCreated
from paddle_billing.Notifications.Entities.Transaction import Transaction

from tests.Utils.ReadsFixture import ReadsFixtures


class TestEventsClient:
    @mark.parametrize(
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                ListEvents(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/events",
            ),
            (
                ListEvents(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/events?order_by=id[asc]&per_page=50",
            ),
            (
                ListEvents(Pager(after="evt_01h83xenpcfjyhkqr4x214m02x")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/events?after=evt_01h83xenpcfjyhkqr4x214m02x&order_by=id[asc]&per_page=50",
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

        events = test_client.client.events.list(operation)
        response_json = test_client.client.events.response.json()
        last_request = mock_requests.last_request

        assert isinstance(events, EventCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

        assert len(events.items) == 11
        for event in events.items:
            assert isinstance(event, Event)
            assert event.event_id is not None
            assert not hasattr(event, "notification_id")

    def test_list_subscription_created_event(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/events",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_default"),
        )

        events = test_client.client.events.list()

        assert isinstance(events, EventCollection)

        subscription_updated_entity = events.items[0].data
        assert isinstance(subscription_updated_entity, Subscription)
        assert not hasattr(subscription_updated_entity, "transaction_id")

        subscription_created_entity = events.items[1].data
        assert isinstance(subscription_created_entity, SubscriptionCreated)
        assert subscription_created_entity.transaction_id == "txn_01hv975mbh902hcyb7mks5kt0n"

    def test_list_transaction_event_with_and_without_payment_method_id(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/events",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_default"),
        )

        events = test_client.client.events.list()

        assert isinstance(events, EventCollection)

        transaction_updated_entity = events.items[9].data

        assert isinstance(transaction_updated_entity, Transaction)

        payment_with_payment_method_id = transaction_updated_entity.payments[0]
        assert payment_with_payment_method_id.payment_method_id == "paymtd_01hkm9xwqpbbpr1ksmvg3sx3v1"

        payment_without_payment_method_id = transaction_updated_entity.payments[1]
        assert payment_without_payment_method_id.payment_method_id is None
