from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionHistoryPausedEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryPausedEffectiveFrom" = member("immediately")
    NextBillingPeriod: "SubscriptionHistoryPausedEffectiveFrom" = member("next_billing_period")
