from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Flat        = 'flat'
    FlatPerSeat = 'flat_per_seat'
    Percentage  = 'percentage'
