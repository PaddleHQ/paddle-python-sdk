from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class EffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextBillingPeriod: "EffectiveFrom" = member("next_billing_period")
    Immediately: "EffectiveFrom" = member("immediately")
