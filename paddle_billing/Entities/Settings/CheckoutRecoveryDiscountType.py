from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class CheckoutRecoveryDiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Percentage: "CheckoutRecoveryDiscountType" = member("percentage")
