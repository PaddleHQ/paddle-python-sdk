from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class MetricsSortDirection(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Asc: "MetricsSortDirection" = member("asc")
    Desc: "MetricsSortDirection" = member("desc")
