from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CheckoutDomainPaymentMethodVerificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Verified: "CheckoutDomainPaymentMethodVerificationStatus" = member("verified")
    Unverified: "CheckoutDomainPaymentMethodVerificationStatus" = member("unverified")
