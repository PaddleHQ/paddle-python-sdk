from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Subscriptions import (
    SubscriptionEffectiveFrom,
    SubscriptionOnPaymentFailure,
)

from paddle_billing.Resources.Subscriptions.Operations.Charge import (
    SubscriptionChargeItem,
    SubscriptionChargeItemWithPrice,
)


@dataclass
class PreviewOneTimeCharge(Operation):
    effective_from: SubscriptionEffectiveFrom
    items: list[SubscriptionChargeItem | SubscriptionChargeItemWithPrice]
    on_payment_failure: SubscriptionOnPaymentFailure | Undefined = Undefined()
