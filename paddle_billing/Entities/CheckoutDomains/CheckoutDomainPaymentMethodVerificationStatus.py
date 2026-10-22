from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CheckoutDomainPaymentMethodVerificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Verified: "CheckoutDomainPaymentMethodVerificationStatus" = "verified"
    Unverified: "CheckoutDomainPaymentMethodVerificationStatus" = "unverified"
