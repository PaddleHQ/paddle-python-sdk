from __future__  import annotations
from .Entity     import Entity
from dataclasses import dataclass
from datetime    import datetime
from typing      import List, Optional

from src.Entities.Shared.BillingDetails                    import BillingDetails
from src.Entities.Shared.CollectionMode                    import CollectionMode
from src.Entities.Shared.CurrencyCode                      import CurrencyCode
from src.Entities.Shared.CustomData                        import CustomData
from src.Entities.Shared.TimePeriod                        import TimePeriod
from src.Entities.Subscription.SubscriptionDiscount        import SubscriptionDiscount
from src.Entities.Subscription.SubscriptionItem            import SubscriptionItem
from src.Entities.Subscription.SubscriptionManagementUrls  import SubscriptionManagementUrls
from src.Entities.Subscription.SubscriptionStatus          import SubscriptionStatus
from src.Entities.Subscription.SubscriptionScheduledChange import SubscriptionScheduledChange
from src.Entities.Subscription.SubscriptionTimePeriod      import SubscriptionTimePeriod


@dataclass
class Subscription(Entity):
    id:                   str
    status:               SubscriptionStatus
    customerId:           str
    addressId:            str
    businessId:           Optional[str]
    currencyCode:         CurrencyCode
    createdAt:            datetime
    updatedAt:            datetime
    startedAt:            Optional[datetime]
    firstBilledAt:        Optional[datetime]
    nextBilledAt:         Optional[datetime]
    pausedAt:             Optional[datetime]
    canceledAt:           Optional[datetime]
    discount:             Optional[SubscriptionDiscount]
    collectionMode:       CollectionMode
    billingDetails:       Optional[BillingDetails]
    currentBillingPeriod: SubscriptionTimePeriod
    billingCycle:         TimePeriod
    scheduledChange:      Optional[SubscriptionScheduledChange]
    managementUrls:       SubscriptionManagementUrls
    items:                List[SubscriptionItem]
    customData:           Optional[CustomData]


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
            startedAt            = datetime.fromisoformat(data['started_at']) if data.get('started_at') else None,
            firstBilledAt        = datetime.fromisoformat(data['first_billed_at']) if data.get('first_billed_at') else None,
            nextBilledAt         = datetime.fromisoformat(data['next_billed_at']) if data.get('next_billed_at') else None,
            pausedAt             = datetime.fromisoformat(data['paused_at']) if data.get('paused_at') else None,
            canceledAt           = datetime.fromisoformat(data['canceled_at']) if data.get('canceled_at') else None,
            discount             = SubscriptionDiscount.from_dict(data['discount']) if data.get('discount') else None,
            collectionMode       = CollectionMode(data['collection_mode']),
            billingDetails       = BillingDetails.from_dict(data['billing_details']) if data.get('billing_details') else None,
            currentBillingPeriod = SubscriptionTimePeriod.from_dict(data['current_billing_period']),
            billingCycle         = TimePeriod.from_dict(data['billing_cycle']),
            scheduledChange      = SubscriptionScheduledChange.from_dict(data['scheduled_change']) if data.get('scheduled_change') else None,
            managementUrls       = SubscriptionManagementUrls.from_dict(data['management_urls']),
            items                = [SubscriptionItem.from_dict(item) for item in data['items']],
            customData           = CustomData(data['custom_data']) if data.get('custom_data') else None,
        )
