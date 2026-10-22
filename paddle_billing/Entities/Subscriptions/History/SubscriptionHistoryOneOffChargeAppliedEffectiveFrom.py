from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionHistoryOneOffChargeAppliedEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryOneOffChargeAppliedEffectiveFrom" = "immediately"
    NextBillingPeriod: "SubscriptionHistoryOneOffChargeAppliedEffectiveFrom" = "next_billing_period"
