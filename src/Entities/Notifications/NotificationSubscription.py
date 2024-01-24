from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Shared.BillingDetails import BillingDetails
from src.Entities.Shared.CollectionMode import CollectionMode
from src.Entities.Shared.CurrencyCode   import CurrencyCode
from src.Entities.Shared.CustomData     import CustomData
from src.Entities.Shared.TimePeriod     import TimePeriod

from src.Entities.Subscriptions.SubscriptionDiscount        import SubscriptionDiscount
from src.Entities.Subscriptions.SubscriptionItem            import SubscriptionItem
from src.Entities.Subscriptions.SubscriptionScheduledChange import SubscriptionScheduledChange
from src.Entities.Subscriptions.SubscriptionStatus          import SubscriptionStatus
from src.Entities.Subscriptions.SubscriptionTimePeriod      import SubscriptionTimePeriod


@dataclass
class NotificationSubscription(Entity):
    id:                   str
    status:               SubscriptionStatus
    customer_id:           str
    addressId:            str
    businessId:           str | None
    currency_code:         CurrencyCode
    created_at:            datetime
    updated_at:            datetime
    startedAt:            datetime | None
    firstBilledAt:        datetime | None
    next_billed_at:         datetime | None
    pausedAt:             datetime | None
    canceledAt:           datetime | None
    discount:             SubscriptionDiscount | None
    collectionMode:       CollectionMode
    billingDetails:       BillingDetails | None
    currentBillingPeriod: SubscriptionTimePeriod
    billing_cycle:         TimePeriod
    scheduledChange:      SubscriptionScheduledChange | None
    items:                list[SubscriptionItem]
    custom_data:           CustomData | None


    @classmethod
    def from_dict(cls, data: dict) -> NotificationSubscription:
        return NotificationSubscription(
            id                   = data['id'],
            status               = SubscriptionStatus(data['status']),
            customer_id           = data['customer_id'],
            addressId            = data['address_id'],
            businessId           = data.get('business_id'),
            currency_code         = CurrencyCode(data['currency_code']),
            created_at            = datetime.fromisoformat(data['created_at']),
            updated_at            = datetime.fromisoformat(data['updated_at']),
            startedAt            = datetime.fromisoformat(data['started_at']) if data.get('started_at') else None,
            firstBilledAt        = datetime.fromisoformat(data['first_billed_at']) if data.get('first_billed_at') else None,
            next_billed_at         = datetime.fromisoformat(data['next_billed_at']) if data.get('next_billed_at') else None,
            pausedAt             = datetime.fromisoformat(data['paused_at']) if data.get('paused_at') else None,
            canceledAt           = datetime.fromisoformat(data['canceled_at']) if data.get('canceled_at') else None,
            discount             = SubscriptionDiscount.from_dict(data['discount']) if data.get('discount') else None,
            collectionMode       = CollectionMode(data['collection_mode']),
            billingDetails       = BillingDetails.from_dict(data['billing_details']) if data.get('billing_details') else None,
            currentBillingPeriod = SubscriptionTimePeriod.from_dict(data['current_billing_period']),
            billing_cycle         = TimePeriod.from_dict(data['billing_cycle']),
            scheduledChange      = SubscriptionScheduledChange.from_dict(data['scheduled_change']) if data.get('scheduled_change') else None,
            items                = [SubscriptionItem.from_dict(item) for item in data['items']],
            custom_data           = CustomData(data['custom_data']) if data.get('custom_data') else None,
        )
