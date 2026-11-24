from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionResumeEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionResumeEffectiveFrom" = member("immediately")
