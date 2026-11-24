from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined

from paddle_billing.Entities.Subscriptions import (
    SubscriptionEffectiveFrom as SubscriptionEffectiveFrom,
    SubscriptionOnPaymentFailure as SubscriptionOnPaymentFailure,
)

from paddle_billing.Resources.Subscriptions.Operations.Charge import (
    SubscriptionChargeItem as SubscriptionChargeItem,
    SubscriptionChargeItemWithPrice as SubscriptionChargeItemWithPrice,
)


@dataclass
class PreviewOneTimeCharge(Operation):
    effective_from: SubscriptionEffectiveFrom
    items: list[SubscriptionChargeItem | SubscriptionChargeItemWithPrice]
    on_payment_failure: SubscriptionOnPaymentFailure | Undefined = Undefined()
