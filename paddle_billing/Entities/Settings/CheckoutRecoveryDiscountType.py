from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CheckoutRecoveryDiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Percentage: "CheckoutRecoveryDiscountType" = member("percentage")
