# mypy: disable-error-code="assignment"
from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionResumeEffectiveFrom(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Immediately: "SubscriptionResumeEffectiveFrom" = "immediately"
