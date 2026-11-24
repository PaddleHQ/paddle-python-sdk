from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CheckoutDomainPaymentMethod(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ApplePay: "CheckoutDomainPaymentMethod" = member("apple_pay")
