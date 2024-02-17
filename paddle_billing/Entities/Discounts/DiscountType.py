from paddle_billing.PaddleStrEnum import PaddleStrEnum


class DiscountType(PaddleStrEnum):
    Flat        = 'flat'
    FlatPerSeat = 'flat_per_seat'
    Percentage  = 'percentage'
