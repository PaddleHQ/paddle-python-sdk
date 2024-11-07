from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Subscriptions import (
    SubscriptionEffectiveFrom,
    SubscriptionItems,
    SubscriptionItemsWithPrice,
    SubscriptionOnPaymentFailure,
)


@dataclass
class PreviewOneTimeCharge(Operation):
    effective_from: SubscriptionEffectiveFrom
    items: list[SubscriptionItems | SubscriptionItemsWithPrice]
    on_payment_failure: SubscriptionOnPaymentFailure | Undefined = Undefined()
