from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class EffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextBillingPeriod: "EffectiveFrom" = "next_billing_period"
    Immediately: "EffectiveFrom" = "immediately"
