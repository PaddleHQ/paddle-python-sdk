from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Flat: "DiscountType" = member("flat")
    FlatPerSeat: "DiscountType" = member("flat_per_seat")
    Percentage: "DiscountType" = member("percentage")
