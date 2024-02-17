from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import (
    BillingDetails,
    CollectionMode,
    CurrencyCode,
    CustomData,
    ImportMeta,
    TimePeriod
)
from paddle_billing.Notifications.Entities.Subscriptions import (
    SubscriptionDiscount,
    SubscriptionItem,
    SubscriptionScheduledChange,
    SubscriptionStatus,
    SubscriptionTimePeriod,
)


@dataclass
class Subscription(Entity):
    address_id:             str
    billing_cycle:          TimePeriod
    collection_mode:        CollectionMode
    created_at:             datetime
    currency_code:          CurrencyCode
    customer_id:            str
    id:                     str
    items:                  list[SubscriptionItem]
    status:                 SubscriptionStatus
    updated_at:             datetime
    billing_details:        BillingDetails              | None = None
    business_id:            str                         | None = None
    canceled_at:            datetime                    | None = None
    current_billing_period: SubscriptionTimePeriod      | None = None
    custom_data:            CustomData                  | None = None
    discount:               SubscriptionDiscount        | None = None
    import_meta:            ImportMeta                  | None = None
    first_billed_at:        datetime                    | None = None
    next_billed_at:         datetime                    | None = None
    paused_at:              datetime                    | None = None
    scheduled_change:       SubscriptionScheduledChange | None = None
    started_at:             datetime                    | None = None
    transaction_id:         str                         | None = None  # Only provided by subscription.created


    @classmethod
    def from_dict(cls, data: dict) -> Subscription:
        return Subscription(
            id                     = data['id'],
            transaction_id         = data.get('transaction_id'),
            status                 = SubscriptionStatus(data['status']),
            customer_id            = data['customer_id'],
            address_id             = data['address_id'],
            business_id            = data.get('business_id'),
            currency_code          = CurrencyCode(data['currency_code']),
            created_at             = datetime.fromisoformat(data['created_at']),
            updated_at             = datetime.fromisoformat(data['updated_at']),
            collection_mode        = CollectionMode(data['collection_mode']),
            billing_cycle          = TimePeriod.from_dict(data['billing_cycle']),
            items                  = [SubscriptionItem.from_dict(item) for item in data['items']],
            billing_details        = BillingDetails.from_dict(data['billing_details']) if data.get('billing_details') else None,
            canceled_at            = datetime.fromisoformat(data['canceled_at'])       if data.get('canceled_at')     else None,
            custom_data            = CustomData(data['custom_data'])                   if data.get('custom_data')     else None,
            discount               = SubscriptionDiscount.from_dict(data['discount'])  if data.get('discount')        else None,
            first_billed_at        = datetime.fromisoformat(data['first_billed_at'])   if data.get('first_billed_at') else None,
            import_meta            = ImportMeta.from_dict(data['import_meta'])         if data.get('import_meta')     else None,
            next_billed_at         = datetime.fromisoformat(data['next_billed_at'])    if data.get('next_billed_at')  else None,
            paused_at              = datetime.fromisoformat(data['paused_at'])         if data.get('paused_at')       else None,
            started_at             = datetime.fromisoformat(data['started_at'])        if data.get('started_at')      else None,
            current_billing_period = SubscriptionTimePeriod.from_dict(data['current_billing_period']) if data.get('billing_details')  else None,
            scheduled_change       = SubscriptionScheduledChange.from_dict(data['scheduled_change'])  if data.get('scheduled_change') else None,
        )
