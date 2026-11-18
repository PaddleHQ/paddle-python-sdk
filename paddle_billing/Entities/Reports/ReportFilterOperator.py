# mypy: disable-error-code="assignment"
from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportFilterOperator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Lt: "ReportFilterOperator" = "lt"
    Gte: "ReportFilterOperator" = "gte"
