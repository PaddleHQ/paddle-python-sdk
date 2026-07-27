from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionHistoryCanceledEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryCanceledEffectiveFrom" = "immediately"
    NextBillingPeriod: "SubscriptionHistoryCanceledEffectiveFrom" = "next_billing_period"
