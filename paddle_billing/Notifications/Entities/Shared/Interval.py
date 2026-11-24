from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Interval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "Interval" = member("day")
    Week: "Interval" = member("week")
    Month: "Interval" = member("month")
    Year: "Interval" = member("year")
