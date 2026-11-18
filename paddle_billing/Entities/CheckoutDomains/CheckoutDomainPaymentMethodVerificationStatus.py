from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class CheckoutDomainPaymentMethodVerificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Verified: "CheckoutDomainPaymentMethodVerificationStatus" = member("verified")
    Unverified: "CheckoutDomainPaymentMethodVerificationStatus" = member("unverified")
