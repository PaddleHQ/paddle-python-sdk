from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Flat: "DiscountType" = "flat"
    FlatPerSeat: "DiscountType" = "flat_per_seat"
    Percentage: "DiscountType" = "percentage"
