from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionConsentRequirementStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "SubscriptionConsentRequirementStatus" = member("pending")
    Granted: "SubscriptionConsentRequirementStatus" = member("granted")
    Voided: "SubscriptionConsentRequirementStatus" = member("voided")
