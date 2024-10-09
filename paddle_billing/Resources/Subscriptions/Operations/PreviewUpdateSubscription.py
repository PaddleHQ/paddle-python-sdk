from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Shared import CollectionMode, CurrencyCode, CustomData
from paddle_billing.Entities.Subscriptions import (
    SubscriptionItems,
    SubscriptionItemsWithPrice,
    SubscriptionOnPaymentFailure,
    SubscriptionProrationBillingMode,
)

from paddle_billing.Resources.Subscriptions.Operations.Update import (
    SubscriptionDiscount,
    UpdateBillingDetails,
)


@dataclass
class PreviewUpdateSubscription(Operation):
    customer_id: str | Undefined = Undefined()
    address_id: str | Undefined = Undefined()
    business_id: str | None | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    next_billed_at: DateTime | Undefined = Undefined()
    discount: SubscriptionDiscount | None | Undefined = Undefined()
    collection_mode: CollectionMode | Undefined = Undefined()
    billing_details: UpdateBillingDetails | None | Undefined = Undefined()
    scheduled_change: None | Undefined = Undefined()
    items: list[SubscriptionItems | SubscriptionItemsWithPrice] | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    proration_billing_mode: SubscriptionProrationBillingMode | Undefined = Undefined()
    on_payment_failure: SubscriptionOnPaymentFailure | Undefined = Undefined()
