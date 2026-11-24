from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class VerificationType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Onboarding: "VerificationType" = member("onboarding")
    Domain: "VerificationType" = member("domain")
