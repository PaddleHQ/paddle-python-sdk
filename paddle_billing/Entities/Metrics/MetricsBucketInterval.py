from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class MetricsBucketInterval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "MetricsBucketInterval" = member("day")
    Week: "MetricsBucketInterval" = member("week")
    Month: "MetricsBucketInterval" = member("month")
