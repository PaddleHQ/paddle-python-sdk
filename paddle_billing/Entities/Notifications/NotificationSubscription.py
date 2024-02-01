from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Entity import Entity

from paddle_billing.Entities.Shared.BillingDetails import BillingDetails
from paddle_billing.Entities.Shared.CollectionMode import CollectionMode
from paddle_billing.Entities.Shared.CurrencyCode   import CurrencyCode
from paddle_billing.Entities.Shared.CustomData     import CustomData
from paddle_billing.Entities.Shared.TimePeriod     import TimePeriod

from paddle_billing.Entities.Subscriptions.SubscriptionDiscount        import SubscriptionDiscount
from paddle_billing.Entities.Subscriptions.SubscriptionItem            import SubscriptionItem
from paddle_billing.Entities.Subscriptions.SubscriptionScheduledChange import SubscriptionScheduledChange
from paddle_billing.Entities.Subscriptions.SubscriptionStatus          import SubscriptionStatus
from paddle_billing.Entities.Subscriptions.SubscriptionTimePeriod      import SubscriptionTimePeriod


@dataclass
class NotificationSubscription(Entity):
    id:                     str
    status:                 SubscriptionStatus
    customer_id:            str
    address_id:             str
    business_id:            str | None
    currency_code:          CurrencyCode
    created_at:             datetime
    updated_at:             datetime
    collection_mode:        CollectionMode
    current_billing_period: SubscriptionTimePeriod
    billing_cycle:          TimePeriod
    items:                  list[SubscriptionItem]
    started_at:             datetime                    | None = None
    first_billed_at:        datetime                    | None = None
    next_billed_at:         datetime                    | None = None
    paused_at:              datetime                    | None = None
    canceled_at:            datetime                    | None = None
    discount:               SubscriptionDiscount        | None = None
    billing_details:        BillingDetails              | None = None
    scheduled_change:       SubscriptionScheduledChange | None = None
    custom_data:            CustomData                  | None = None


    @classmethod
    def from_dict(cls, data: dict) -> NotificationSubscription:
        return NotificationSubscription(
            id                     = data['id'],
            status                 = SubscriptionStatus(data['status']),
            customer_id            = data['customer_id'],
            address_id             = data['address_id'],
            business_id            = data.get('business_id'),
            currency_code          = CurrencyCode(data['currency_code']),
            created_at             = datetime.fromisoformat(data['created_at']),
            updated_at             = datetime.fromisoformat(data['updated_at']),
            collection_mode        = CollectionMode(data['collection_mode']),
            current_billing_period = SubscriptionTimePeriod.from_dict(data['current_billing_period']),
            billing_cycle          = TimePeriod.from_dict(data['billing_cycle']),
            items                  = [SubscriptionItem.from_dict(item) for item in data['items']],
            started_at             = datetime.fromisoformat(data['started_at'])        if data.get('started_at')      else None,
            first_billed_at        = datetime.fromisoformat(data['first_billed_at'])   if data.get('first_billed_at') else None,
            next_billed_at         = datetime.fromisoformat(data['next_billed_at'])    if data.get('next_billed_at')  else None,
            paused_at              = datetime.fromisoformat(data['paused_at'])         if data.get('paused_at')       else None,
            canceled_at            = datetime.fromisoformat(data['canceled_at'])       if data.get('canceled_at')     else None,
            discount               = SubscriptionDiscount.from_dict(data['discount'])  if data.get('discount')        else None,
            billing_details        = BillingDetails.from_dict(data['billing_details']) if data.get('billing_details') else None,
            custom_data            = CustomData(data['custom_data'])                   if data.get('custom_data')     else None,
            scheduled_change       = (SubscriptionScheduledChange.from_dict(data['scheduled_change'])
                                      if data.get('scheduled_change')
                                      else None),
        )