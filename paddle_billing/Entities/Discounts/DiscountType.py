from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Flat: "DiscountType" = member("flat")
    FlatPerSeat: "DiscountType" = member("flat_per_seat")
    Percentage: "DiscountType" = member("percentage")
