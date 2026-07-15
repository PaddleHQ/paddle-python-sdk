from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CheckoutDomainPaymentMethod(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ApplePay: "CheckoutDomainPaymentMethod" = "apple_pay"
