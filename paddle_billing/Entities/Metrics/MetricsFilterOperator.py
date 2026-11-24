from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class MetricsFilterOperator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    In: "MetricsFilterOperator" = member("in")
