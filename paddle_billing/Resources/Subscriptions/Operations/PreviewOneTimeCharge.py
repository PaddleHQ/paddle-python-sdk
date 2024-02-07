from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Subscriptions import (
    SubscriptionEffectiveFrom,
    SubscriptionItems,
    SubscriptionItemsWithPrice,
    SubscriptionOnPaymentFailure,
)


@dataclass
class PreviewOneTimeCharge:
    effective_from:     SubscriptionEffectiveFrom
    items:              list[SubscriptionItems | SubscriptionItemsWithPrice]
    on_payment_failure: SubscriptionOnPaymentFailure | Undefined = Undefined()
    receipt_data:       str                          | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
