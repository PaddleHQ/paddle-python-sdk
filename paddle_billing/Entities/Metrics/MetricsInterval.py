from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class MetricsInterval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "MetricsInterval" = member("day")
