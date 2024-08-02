from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Interval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day   = 'day'
    Week  = 'week'
    Month = 'month'
    Year  = 'year'
