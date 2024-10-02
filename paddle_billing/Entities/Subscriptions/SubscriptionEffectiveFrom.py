from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextBillingPeriod: "SubscriptionEffectiveFrom" = "next_billing_period"
    Immediately: "SubscriptionEffectiveFrom" = "immediately"
