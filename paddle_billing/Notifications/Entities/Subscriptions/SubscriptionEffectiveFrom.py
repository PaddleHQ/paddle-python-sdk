from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextBillingPeriod: "SubscriptionEffectiveFrom" = member("next_billing_period")
    Immediately: "SubscriptionEffectiveFrom" = member("immediately")
