from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class EffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextBillingPeriod: "EffectiveFrom" = member("next_billing_period")
    Immediately: "EffectiveFrom" = member("immediately")
