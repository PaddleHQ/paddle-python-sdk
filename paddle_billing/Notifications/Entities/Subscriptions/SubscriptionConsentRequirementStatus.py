from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionConsentRequirementStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "SubscriptionConsentRequirementStatus" = member("pending")
    Granted: "SubscriptionConsentRequirementStatus" = member("granted")
    Voided: "SubscriptionConsentRequirementStatus" = member("voided")
