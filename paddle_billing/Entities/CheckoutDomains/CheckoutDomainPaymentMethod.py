from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class CheckoutDomainPaymentMethod(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ApplePay: "CheckoutDomainPaymentMethod" = member("apple_pay")
