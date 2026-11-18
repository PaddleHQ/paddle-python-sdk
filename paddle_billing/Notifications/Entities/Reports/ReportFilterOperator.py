from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ReportFilterOperator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Lt: "ReportFilterOperator" = member("lt")
    Gte: "ReportFilterOperator" = member("gte")
