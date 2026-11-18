from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class Interval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "Interval" = member("day")
    Week: "Interval" = member("week")
    Month: "Interval" = member("month")
    Year: "Interval" = member("year")
