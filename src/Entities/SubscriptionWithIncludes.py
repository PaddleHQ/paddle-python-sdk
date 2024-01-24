from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Shared.BillingDetails            import BillingDetails
from src.Entities.Shared.CollectionMode            import CollectionMode
from src.Entities.Shared.CurrencyCode              import CurrencyCode
from src.Entities.Shared.CustomData                import CustomData
from src.Entities.Shared.TimePeriod                import TimePeriod
from src.Entities.Shared.TransactionDetailsPreview import TransactionDetailsPreview

from src.Entities.Subscriptions.SubscriptionDiscount        import SubscriptionDiscount
from src.Entities.Subscriptions.SubscriptionItem            import SubscriptionItem
from src.Entities.Subscriptions.SubscriptionManagementUrls  import SubscriptionManagementUrls
from src.Entities.Subscriptions.SubscriptionNextTransaction import SubscriptionNextTransaction
from src.Entities.Subscriptions.SubscriptionScheduledChange import SubscriptionScheduledChange
from src.Entities.Subscriptions.SubscriptionStatus          import SubscriptionStatus
from src.Entities.Subscriptions.SubscriptionTimePeriod      import SubscriptionTimePeriod


@dataclass
class SubscriptionWithIncludes(Entity):
    id:                          str
    status:                      SubscriptionStatus
    customerId:                  str
    addressId:                   str
    businessId:                  str | None
    currencyCode:                CurrencyCode
    createdAt:                   datetime
    updatedAt:                   datetime
    startedAt:                   datetime | None
    firstBilledAt:               datetime | None
    nextBilledAt:                datetime | None
    pausedAt:                    datetime | None
    canceledAt:                  datetime | None
    discount:                    SubscriptionDiscount | None
    collectionMode:              CollectionMode
    billingDetails:              BillingDetails | None
    currentBillingPeriod:        SubscriptionTimePeriod | None
    billingCycle:                TimePeriod
    scheduledChange:             SubscriptionScheduledChange | None
    managementUrls:              SubscriptionManagementUrls | None
    items:                       list[SubscriptionItem]
    customData:                  CustomData | None
    nextTransaction:             SubscriptionNextTransaction | None
    recurringTransactionDetails: TransactionDetailsPreview | None


    @classmethod
    def from_dict(cls, data: dict) -> SubscriptionWithIncludes:
        return SubscriptionWithIncludes(
            id                          = data['id'],
            status                      = SubscriptionStatus(data['status']),
            customerId                  = data['customer_id'],
            addressId                   = data['address_id'],
            businessId                  = data.get('business_id'),
            currencyCode                = CurrencyCode(data['currency_code']),
            createdAt                   = datetime.fromisoformat(data['created_at']),
            updatedAt                   = datetime.fromisoformat(data['updated_at']),
            startedAt                   = datetime.fromisoformat(data['started_at']) if 'started_at' in data else None,
            firstBilledAt               = datetime.fromisoformat(data['first_billed_at']) if 'first_billed_at' in data else None,
            nextBilledAt                = datetime.fromisoformat(data['next_billed_at']) if 'next_billed_at' in data else None,
            pausedAt                    = datetime.fromisoformat(data['paused_at']) if 'paused_at' in data else None,
            canceledAt                  = datetime.fromisoformat(data['canceled_at']) if 'canceled_at' in data else None,
            discount                    = SubscriptionDiscount.from_dict(data['discount']) if 'discount' in data else None,
            collectionMode              = CollectionMode(data['collection_mode']),
            billingDetails              = BillingDetails.from_dict(data['billing_details']) if 'billing_details' in data else None,
            currentBillingPeriod        = SubscriptionTimePeriod.from_dict(data['current_billing_period']) if 'current_billing_period' in data else None,
            billingCycle                = TimePeriod.from_dict(data['billing_cycle']),
            scheduledChange             = SubscriptionScheduledChange.from_dict(data['scheduled_change']) if 'scheduled_change' in data else None,
            managementUrls              = SubscriptionManagementUrls.from_dict(data['management_urls']) if 'management_urls' in data else None,
            items                       = [SubscriptionItem.from_dict(item) for item in data['items']],
            customData                  = CustomData(data['custom_data']) if 'custom_data' in data else None,
            nextTransaction             = SubscriptionNextTransaction.from_dict(data['next_transaction']) if 'next_transaction' in data else None,
            recurringTransactionDetails = TransactionDetailsPreview.from_dict(data['recurring_transaction_details']) if 'recurring_transaction_details' in data else None,
        )
