from enum import StrEnum


class DiscountType(StrEnum):
    Flat        = 'flat'
    FlatPerSeat = 'flat_per_seat'
    Percentage  = 'percentage'
