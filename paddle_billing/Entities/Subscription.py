from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Entity import Entity

from paddle_billing.Entities.Shared.TransactionDetailsPreview import TransactionDetailsPreview
from paddle_billing.Entities.Shared import (
    BillingDetails,
    CollectionMode,
    CurrencyCode,
    CustomData,
    ImportMeta,
    TimePeriod,
)

from paddle_billing.Entities.Subscriptions import (
    SubscriptionDiscount,
    SubscriptionItem,
    SubscriptionManagementUrls,
    SubscriptionNextTransaction,
    SubscriptionScheduledChange,
    SubscriptionStatus,
    SubscriptionTimePeriod,
)


@dataclass
class Subscription(Entity):
    id:                            str
    status:                        SubscriptionStatus
    customer_id:                   str
    address_id:                    str
    business_id:                   str | None
    currency_code:                 CurrencyCode
    created_at:                    datetime
    updated_at:                    datetime
    started_at:                    datetime             | None
    first_billed_at:               datetime             | None
    next_billed_at:                datetime             | None
    paused_at:                     datetime             | None
    canceled_at:                   datetime             | None
    discount:                      SubscriptionDiscount | None
    collection_mode:               CollectionMode
    billing_details:               BillingDetails         | None
    current_billing_period:        SubscriptionTimePeriod | None
    billing_cycle:                 TimePeriod
    scheduled_change:              SubscriptionScheduledChange | None
    management_urls:               SubscriptionManagementUrls  | None
    items:                         list[SubscriptionItem]
    next_transaction:              SubscriptionNextTransaction | None
    recurring_transaction_details: TransactionDetailsPreview   | None
    import_meta:                   ImportMeta                  | None = None
    custom_data:                   CustomData                  | None = None


    @classmethod
    def from_dict(cls, data: dict) -> Subscription:
        return Subscription(
            id                     = data['id'],
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
            current_billing_period = SubscriptionTimePeriod.from_dict(data['current_billing_period']) if data.get('current_billing_period') else None,
            management_urls        = SubscriptionManagementUrls.from_dict(data['management_urls'])    if data.get('management_urls')        else None,
            started_at             = datetime.fromisoformat(data['started_at'])                       if data.get('started_at')             else None,
            first_billed_at        = datetime.fromisoformat(data['first_billed_at'])                  if data.get('first_billed_at')        else None,
            next_billed_at         = datetime.fromisoformat(data['next_billed_at'])                   if data.get('next_billed_at')         else None,
            paused_at              = datetime.fromisoformat(data['paused_at'])                        if data.get('paused_at')              else None,
            canceled_at            = datetime.fromisoformat(data['canceled_at'])                      if data.get('canceled_at')            else None,
            discount               = SubscriptionDiscount.from_dict(data['discount'])                 if data.get('discount')               else None,
            billing_details        = BillingDetails.from_dict(data['billing_details'])                if data.get('billing_details')        else None,
            scheduled_change       = SubscriptionScheduledChange.from_dict(data['scheduled_change'])  if data.get('scheduled_change')       else None,
            custom_data            = CustomData(data['custom_data'])                                  if data.get('custom_data')            else None,
            import_meta            = ImportMeta.from_dict(data['import_meta'])                        if data.get('import_meta')            else None,
            next_transaction       = SubscriptionNextTransaction.from_dict(data['next_transaction'])  if data.get('next_transaction')       else None,

            recurring_transaction_details = TransactionDetailsPreview.from_dict(data['recurring_transaction_details']) if data.get('recurring_transaction_details') else None,
        )
