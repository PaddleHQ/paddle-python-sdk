from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class VerificationType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Onboarding: "VerificationType" = member("onboarding")
    Domain: "VerificationType" = member("domain")
