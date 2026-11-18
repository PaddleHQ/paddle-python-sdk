from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class MetricsSortDirection(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Asc: "MetricsSortDirection" = member("asc")
    Desc: "MetricsSortDirection" = member("desc")
