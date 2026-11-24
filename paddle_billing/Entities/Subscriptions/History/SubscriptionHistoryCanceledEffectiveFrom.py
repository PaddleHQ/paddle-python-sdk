from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionHistoryCanceledEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryCanceledEffectiveFrom" = member("immediately")
    NextBillingPeriod: "SubscriptionHistoryCanceledEffectiveFrom" = member("next_billing_period")
