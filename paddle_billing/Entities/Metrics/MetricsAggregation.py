from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class MetricsAggregation(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Count: "MetricsAggregation" = member("count")
    CountDistinct: "MetricsAggregation" = member("count_distinct")
    Sum: "MetricsAggregation" = member("sum")
