from __future__  import annotations
from .Entity     import Entity
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Shared.BillingDetails import BillingDetails
from src.Entities.Shared.CollectionMode import CollectionMode
from src.Entities.Shared.CurrencyCode   import CurrencyCode
from src.Entities.Shared.CustomData     import CustomData
from src.Entities.Shared.TimePeriod     import TimePeriod

from src.Entities.Subscriptions.SubscriptionDiscount        import SubscriptionDiscount
from src.Entities.Subscriptions.SubscriptionItem            import SubscriptionItem
from src.Entities.Subscriptions.SubscriptionManagementUrls  import SubscriptionManagementUrls
from src.Entities.Subscriptions.SubscriptionStatus          import SubscriptionStatus
from src.Entities.Subscriptions.SubscriptionScheduledChange import SubscriptionScheduledChange
from src.Entities.Subscriptions.SubscriptionTimePeriod      import SubscriptionTimePeriod


@dataclass
class Subscription(Entity):
    id:                   str
    status:               SubscriptionStatus
    customerId:           str
    addressId:            str
    businessId:           str | None
    currencyCode:         CurrencyCode
    createdAt:            datetime
    updatedAt:            datetime
    startedAt:            datetime | None
    firstBilledAt:        datetime | None
    nextBilledAt:         datetime | None
    pausedAt:             datetime | None
    canceledAt:           datetime | None
    discount:             SubscriptionDiscount | None
    collectionMode:       CollectionMode
    billingDetails:       BillingDetails | None
    currentBillingPeriod: SubscriptionTimePeriod
    billingCycle:         TimePeriod
    scheduledChange:      SubscriptionScheduledChange | None
    managementUrls:       SubscriptionManagementUrls
    items:                list[SubscriptionItem]
    customData:           CustomData | None


    @classmethod
    def from_dict(cls, data: dict) -> Subscription:
        return Subscription(
            id                   = data['id'],
            status               = SubscriptionStatus(data['status']),
            customerId           = data['customer_id'],
            addressId            = data['address_id'],
            businessId           = data.get('business_id'),
            currencyCode         = CurrencyCode(data['currency_code']),
            createdAt            = datetime.fromisoformat(data['created_at']),
            updatedAt            = datetime.fromisoformat(data['updated_at']),
            startedAt            = datetime.fromisoformat(data['started_at']) if 'started_at' in data else None,
            firstBilledAt        = datetime.fromisoformat(data['first_billed_at']) if 'first_billed_at' in data else None,
            nextBilledAt         = datetime.fromisoformat(data['next_billed_at']) if 'next_billed_at' in data else None,
            pausedAt             = datetime.fromisoformat(data['paused_at']) if 'paused_at' in data else None,
            canceledAt           = datetime.fromisoformat(data['canceled_at']) if 'canceled_at' in data else None,
            discount             = SubscriptionDiscount.from_dict(data['discount']) if 'discount' in data else None,
            collectionMode       = CollectionMode(data['collection_mode']),
            billingDetails       = BillingDetails.from_dict(data['billing_details']) if 'billing_details' in data else None,
            currentBillingPeriod = SubscriptionTimePeriod.from_dict(data['current_billing_period']),
            billingCycle         = TimePeriod.from_dict(data['billing_cycle']),
            scheduledChange      = SubscriptionScheduledChange.from_dict(data['scheduled_change']) if 'scheduled_change' in data else None,
            managementUrls       = SubscriptionManagementUrls.from_dict(data['management_urls']),
            items                = [SubscriptionItem.from_dict(item) for item in data['items']],
            customData           = CustomData(data['custom_data']) if data.get('custom_data') else None,
        )
