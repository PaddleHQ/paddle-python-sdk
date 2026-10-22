from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class MetricsAggregation(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Count: "MetricsAggregation" = "count"
    CountDistinct: "MetricsAggregation" = "count_distinct"
    Sum: "MetricsAggregation" = "sum"
