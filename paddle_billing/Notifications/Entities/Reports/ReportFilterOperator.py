from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ReportFilterOperator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Lt: "ReportFilterOperator" = member("lt")
    Gte: "ReportFilterOperator" = member("gte")
