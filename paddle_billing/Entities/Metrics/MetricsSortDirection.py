from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class MetricsSortDirection(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Asc: "MetricsSortDirection" = "asc"
    Desc: "MetricsSortDirection" = "desc"
