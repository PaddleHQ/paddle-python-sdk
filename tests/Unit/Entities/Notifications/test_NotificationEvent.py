from json import loads
from pytest import mark
from importlib import import_module

from paddle_billing.Entities.Notifications import NotificationEvent

from paddle_billing.Notifications.Entities.Subscription import Subscription
from paddle_billing.Notifications.Entities.SubscriptionCreated import SubscriptionCreated
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity

from tests.Utils.ReadsFixture import ReadsFixtures


class TestNotificationEvent:
    @mark.parametrize(
        "event_type, entity_name",
        [
            ("address.created", "Address"),
            ("address.imported", "Address"),
            ("address.updated", "Address"),
            ("adjustment.created", "Adjustment"),
            ("adjustment.updated", "Adjustment"),
            ("business.created", "Business"),
            ("business.imported", "Business"),
            ("business.updated", "Business"),
            ("customer.created", "Customer"),
            ("customer.imported", "Customer"),
            ("customer.updated", "Customer"),
            ("discount.created", "Discount"),
            ("discount.imported", "Discount"),
            ("discount.updated", "Discount"),
            ("payment_method.deleted", "PaymentMethodDeleted"),
            ("payment_method.saved", "PaymentMethod"),
            ("payout.created", "Payout"),
            ("payout.paid", "Payout"),
            ("price.created", "Price"),
            ("price.updated", "Price"),
            ("price.imported", "Price"),
            ("product.created", "Product"),
            ("product.updated", "Product"),
            ("product.imported", "Product"),
            ("subscription.activated", "Subscription"),
            ("subscription.canceled", "Subscription"),
            ("subscription.created", "SubscriptionCreated"),
            ("subscription.imported", "Subscription"),
            ("subscription.past_due", "Subscription"),
            ("subscription.paused", "Subscription"),
            ("subscription.resumed", "Subscription"),
            ("subscription.trialing", "Subscription"),
            ("subscription.updated", "Subscription"),
            ("transaction.billed", "Transaction"),
            ("transaction.canceled", "Transaction"),
            ("transaction.completed", "Transaction"),
            ("transaction.created", "Transaction"),
            ("transaction.paid", "Transaction"),
            ("transaction.past_due", "Transaction"),
            ("transaction.payment_failed", "Transaction"),
            ("transaction.ready", "Transaction"),
            ("transaction.updated", "Transaction"),
            ("report.created", "Report"),
            ("report.updated", "Report"),
        ],
        ids=[
            "address.created",
            "address.imported",
            "address.updated",
            "adjustment.created",
            "adjustment.updated",
            "business.created",
            "business.imported",
            "business.updated",
            "customer.created",
            "customer.imported",
            "customer.updated",
            "discount.created",
            "discount.imported",
            "discount.updated",
            "payment_method.deleted",
            "payment_method.saved",
            "payout.created",
            "payout.paid",
            "price.created",
            "price.updated",
            "price.imported",
            "product.created",
            "product.updated",
            "product.imported",
            "subscription.activated",
            "subscription.canceled",
            "subscription.created",
            "subscription.imported",
            "subscription.past_due",
            "subscription.paused",
            "subscription.resumed",
            "subscription.trialing",
            "subscription.updated",
            "transaction.billed",
            "transaction.canceled",
            "transaction.completed",
            "transaction.created",
            "transaction.paid",
            "transaction.past_due",
            "transaction.payment_failed",
            "transaction.ready",
            "transaction.updated",
            "report.created",
            "report.updated",
        ],
    )
    def test_notification_event_from_dict(
        self,
        event_type,
        entity_name,
    ):
        entity_module_path = "paddle_billing.Notifications.Entities"

        imported_module = import_module(f"{entity_module_path}.{entity_name}")
        entity_class = getattr(imported_module, entity_name)

        notification_event = NotificationEvent.from_dict(
            {
                "data": loads(ReadsFixtures.read_raw_json_fixture(f"notification/entity/{event_type}")),
                "notification_id": "ntf_01h8bkrfe7w1vwf8xmytwn51e7",
                "event_type": event_type,
                "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
                "occurred_at": "2023-08-21T11:57:47.390028Z",
            }
        )

        assert isinstance(notification_event.data, entity_class)
        assert notification_event.notification_id == "ntf_01h8bkrfe7w1vwf8xmytwn51e7"
        assert notification_event.event_id == "evt_01h8bzakzx3hm2fmen703n5q45"
        assert notification_event.event_type == event_type
        assert notification_event.occurred_at.isoformat() == "2023-08-21T11:57:47.390028+00:00"
        assert isinstance(notification_event.data.to_dict(), dict)
        assert notification_event.data.to_dict()["id"] is not None

    def test_subscription_created_notification_event_transaction_id(self):
        notification_event = NotificationEvent.from_dict(
            {
                "data": loads(ReadsFixtures.read_raw_json_fixture("notification/entity/subscription.created")),
                "notification_id": "ntf_01h8bkrfe7w1vwf8xmytwn51e7",
                "event_type": "subscription.created",
                "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
                "occurred_at": "2023-08-21T11:57:47.390028Z",
            }
        )

        assert isinstance(notification_event.data, SubscriptionCreated)
        assert notification_event.data.transaction_id == "txn_01hv8wptq8987qeep44cyrewp9"
        assert isinstance(notification_event.data.to_dict(), dict)
        assert notification_event.data.to_dict()["transaction_id"] == "txn_01hv8wptq8987qeep44cyrewp9"

    @mark.parametrize(
        "event_type",
        [
            ("subscription.activated"),
            ("subscription.canceled"),
            ("subscription.imported"),
            ("subscription.past_due"),
            ("subscription.paused"),
            ("subscription.resumed"),
            ("subscription.trialing"),
            ("subscription.updated"),
        ],
        ids=[
            "subscription.activated",
            "subscription.canceled",
            "subscription.imported",
            "subscription.past_due",
            "subscription.paused",
            "subscription.resumed",
            "subscription.trialing",
            "subscription.updated",
        ],
    )
    def test_subscription_notification_events_without_transaction_id(
        self,
        event_type,
    ):

        notification_event = NotificationEvent.from_dict(
            {
                "data": loads(ReadsFixtures.read_raw_json_fixture(f"notification/entity/{event_type}")),
                "notification_id": "ntf_01h8bkrfe7w1vwf8xmytwn51e7",
                "event_type": event_type,
                "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
                "occurred_at": "2023-08-21T11:57:47.390028Z",
            }
        )

        assert isinstance(notification_event.data, Subscription)
        assert not hasattr(notification_event.data, "transaction_id")

    def test_unknown_event_type_is_handled(self):
        notification_event = NotificationEvent.from_dict(
            {
                "data": loads(ReadsFixtures.read_raw_json_fixture("notification/entity/address.created")),
                "notification_id": "ntf_01h8bkrfe7w1vwf8xmytwn51e7",
                "event_type": "some_unknown_entity.created",
                "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
                "occurred_at": "2023-08-21T11:57:47.390028Z",
            }
        )

        assert notification_event.notification_id == "ntf_01h8bkrfe7w1vwf8xmytwn51e7"
        assert notification_event.event_id == "evt_01h8bzakzx3hm2fmen703n5q45"
        assert notification_event.event_type == "some_unknown_entity.created"
        assert notification_event.occurred_at.isoformat() == "2023-08-21T11:57:47.390028+00:00"
        assert isinstance(notification_event.data, UndefinedEntity)
        assert notification_event.data.to_dict()["id"] == "add_01hv8gq3318ktkfengj2r75gfx"

    def test_subscription_notification_event_with_null_discount(self):
        notification_event = NotificationEvent.from_dict(
            {
                "data": loads(ReadsFixtures.read_raw_json_fixture("notification/entity/subscription.trialing")),
                "notification_id": "ntf_01h8bkrfe7w1vwf8xmytwn51e7",
                "event_type": "subscription.trialing",
                "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
                "occurred_at": "2023-08-21T11:57:47.390028Z",
            }
        )

        assert isinstance(notification_event.data, Subscription)
        assert notification_event.data.discount is None

    def test_subscription_notification_event_discount_without_starts_and_ends_at(self):
        notification_event = NotificationEvent.from_dict(
            {
                "data": loads(ReadsFixtures.read_raw_json_fixture("notification/entity/subscription.paused")),
                "notification_id": "ntf_01h8bkrfe7w1vwf8xmytwn51e7",
                "event_type": "subscription.paused",
                "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
                "occurred_at": "2023-08-21T11:57:47.390028Z",
            }
        )

        assert isinstance(notification_event.data, Subscription)
        assert notification_event.data.discount.starts_at is None
        assert notification_event.data.discount.ends_at is None

    def test_subscription_notification_event_with_discount(self):
        notification_event = NotificationEvent.from_dict(
            {
                "data": loads(ReadsFixtures.read_raw_json_fixture("notification/entity/subscription.created")),
                "notification_id": "ntf_01h8bkrfe7w1vwf8xmytwn51e7",
                "event_type": "subscription.created",
                "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
                "occurred_at": "2023-08-21T11:57:47.390028Z",
            }
        )

        assert isinstance(notification_event.data, SubscriptionCreated)
        assert notification_event.data.discount.starts_at.isoformat() == "2024-04-12T10:18:47.635628+00:00"
        assert notification_event.data.discount.ends_at.isoformat() == "2024-05-12T10:18:47.635628+00:00"
