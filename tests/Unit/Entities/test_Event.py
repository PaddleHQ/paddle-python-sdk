from json         import loads
from pytest       import mark
from importlib    import import_module

from paddle_billing.Entities.Event import Event

from paddle_billing.Notifications.Entities.Subscription import Subscription

from tests.Utils.ReadsFixture import ReadsFixtures


class TestEvent:
    @mark.parametrize(
        'event_type, entity_name',
        [
            ('address.created', 'Address'),
            ('address.imported', 'Address'),
            ('address.updated', 'Address'),
            ('adjustment.created', 'Adjustment'),
            ('adjustment.updated', 'Adjustment'),
            ('business.created', 'Business'),
            ('business.imported', 'Business'),
            ('business.updated', 'Business'),
            ('customer.created', 'Customer'),
            ('customer.imported', 'Customer'),
            ('customer.updated', 'Customer'),
            ('discount.created', 'Discount'),
            ('discount.imported', 'Discount'),
            ('discount.updated', 'Discount'),
            ('payout.created', 'Payout'),
            ('payout.paid', 'Payout'),
            ('price.created', 'Price'),
            ('price.updated', 'Price'),
            ('price.imported', 'Price'),
            ('product.created', 'Product'),
            ('product.updated', 'Product'),
            ('product.imported', 'Product'),
            ('subscription.activated', 'Subscription'),
            ('subscription.canceled', 'Subscription'),
            ('subscription.created', 'Subscription'),
            ('subscription.imported', 'Subscription'),
            ('subscription.past_due', 'Subscription'),
            ('subscription.paused', 'Subscription'),
            ('subscription.resumed', 'Subscription'),
            ('subscription.trialing', 'Subscription'),
            ('subscription.updated', 'Subscription'),
            ('transaction.billed', 'Transaction'),
            ('transaction.canceled', 'Transaction'),
            ('transaction.completed', 'Transaction'),
            ('transaction.created', 'Transaction'),
            ('transaction.paid', 'Transaction'),
            ('transaction.past_due', 'Transaction'),
            ('transaction.payment_failed', 'Transaction'),
            ('transaction.ready', 'Transaction'),
            ('transaction.updated', 'Transaction'),
            ('report.created', 'Report'),
            ('report.updated', 'Report'),
        ],
        ids=[
            'address.created',
            'address.imported',
            'address.updated',
            'adjustment.created',
            'adjustment.updated',
            'business.created',
            'business.imported',
            'business.updated',
            'customer.created',
            'customer.imported',
            'customer.updated',
            'discount.created',
            'discount.imported',
            'discount.updated',
            'payout.created',
            'payout.paid',
            'price.created',
            'price.updated',
            'price.imported',
            'product.created',
            'product.updated',
            'product.imported',
            'subscription.activated',
            'subscription.canceled',
            'subscription.created',
            'subscription.imported',
            'subscription.past_due',
            'subscription.paused',
            'subscription.resumed',
            'subscription.trialing',
            'subscription.updated',
            'transaction.billed',
            'transaction.canceled',
            'transaction.completed',
            'transaction.created',
            'transaction.paid',
            'transaction.past_due',
            'transaction.payment_failed',
            'transaction.ready',
            'transaction.updated',
            'report.created',
            'report.updated',
        ]
    )
    def test_event_from_dict(
        self,
        event_type,
        entity_name,
    ):
        entity_module_path = 'paddle_billing.Notifications.Entities'

        imported_module = import_module(f"{entity_module_path}.{entity_name}")
        entity_class    = getattr(imported_module, entity_name)

        event = Event.from_dict({
            "data": loads(ReadsFixtures.read_raw_json_fixture(f"notification/entity/{event_type}")),
            "event_type": event_type,
            "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
            "occurred_at": "2023-08-21T11:57:47.390028Z",
        })

        assert isinstance(event.data, entity_class)
        assert event.event_id == 'evt_01h8bzakzx3hm2fmen703n5q45'
        assert event.event_type == event_type
        assert event.occurred_at.isoformat() == '2023-08-21T11:57:47.390028+00:00'


    @mark.parametrize(
        'event_type, expected_transaction_id',
        [
            ('subscription.created', 'txn_01hv8wptq8987qeep44cyrewp9'),
            ('subscription.activated', None),
            ('subscription.canceled', None),
            ('subscription.imported', None),
            ('subscription.past_due', None),
            ('subscription.paused', None),
            ('subscription.resumed', None),
            ('subscription.trialing', None),
            ('subscription.updated', None),
        ],
        ids=[
            'subscription.created',
            'subscription.activated',
            'subscription.canceled',
            'subscription.imported',
            'subscription.past_due',
            'subscription.paused',
            'subscription.resumed',
            'subscription.trialing',
            'subscription.updated',
        ]
    )
    def test_subscription_event_transaction_id(
        self,
        event_type,
        expected_transaction_id,
    ):

        event = Event.from_dict({
            "data": loads(ReadsFixtures.read_raw_json_fixture(f"notification/entity/{event_type}")),
            "event_type": event_type,
            "event_id": "evt_01h8bzakzx3hm2fmen703n5q45",
            "occurred_at": "2023-08-21T11:57:47.390028Z",
            "notification_id": "ntf_01h8bzam1z32agrxjwhjgqk8w6"
        })

        assert isinstance(event.data, Subscription)
        assert event.data.transaction_id == expected_transaction_id
