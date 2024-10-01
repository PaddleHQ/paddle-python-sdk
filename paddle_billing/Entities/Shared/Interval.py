from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Interval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "Interval" = "day"
    Week: "Interval" = "week"
    Month: "Interval" = "month"
    Year: "Interval" = "year"
