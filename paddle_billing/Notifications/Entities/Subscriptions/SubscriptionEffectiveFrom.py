from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextBillingPeriod: "SubscriptionEffectiveFrom" = member("next_billing_period")
    Immediately: "SubscriptionEffectiveFrom" = member("immediately")
