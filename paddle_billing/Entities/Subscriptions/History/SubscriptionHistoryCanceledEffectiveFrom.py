from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionHistoryCanceledEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionHistoryCanceledEffectiveFrom" = member("immediately")
    NextBillingPeriod: "SubscriptionHistoryCanceledEffectiveFrom" = member("next_billing_period")
