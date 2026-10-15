from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class MetricsBucketInterval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "MetricsBucketInterval" = "day"
    Week: "MetricsBucketInterval" = "week"
    Month: "MetricsBucketInterval" = "month"
