from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionHistoryPausedEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryPausedEffectiveFrom" = "immediately"
    NextBillingPeriod: "SubscriptionHistoryPausedEffectiveFrom" = "next_billing_period"
