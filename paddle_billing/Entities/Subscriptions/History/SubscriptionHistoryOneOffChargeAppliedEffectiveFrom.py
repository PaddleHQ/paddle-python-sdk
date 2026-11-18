from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionHistoryOneOffChargeAppliedEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryOneOffChargeAppliedEffectiveFrom" = member("immediately")
    NextBillingPeriod: "SubscriptionHistoryOneOffChargeAppliedEffectiveFrom" = member("next_billing_period")
