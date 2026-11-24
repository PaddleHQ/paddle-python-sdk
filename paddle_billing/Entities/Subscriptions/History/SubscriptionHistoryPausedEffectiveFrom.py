from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionHistoryPausedEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryPausedEffectiveFrom" = member("immediately")
    NextBillingPeriod: "SubscriptionHistoryPausedEffectiveFrom" = member("next_billing_period")
