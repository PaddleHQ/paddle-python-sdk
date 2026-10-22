from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class VerificationType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Onboarding: "VerificationType" = "onboarding"
    Domain: "VerificationType" = "domain"
