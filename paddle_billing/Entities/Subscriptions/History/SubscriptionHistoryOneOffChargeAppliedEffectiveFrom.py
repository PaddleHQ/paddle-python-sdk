from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionHistoryOneOffChargeAppliedEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryOneOffChargeAppliedEffectiveFrom" = member("immediately")
    NextBillingPeriod: "SubscriptionHistoryOneOffChargeAppliedEffectiveFrom" = member("next_billing_period")
