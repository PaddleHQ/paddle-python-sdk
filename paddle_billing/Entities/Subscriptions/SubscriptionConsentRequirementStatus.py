from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionConsentRequirementStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "SubscriptionConsentRequirementStatus" = "pending"
    Granted: "SubscriptionConsentRequirementStatus" = "granted"
    Voided: "SubscriptionConsentRequirementStatus" = "voided"
