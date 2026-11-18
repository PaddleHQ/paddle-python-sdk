from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class MetricsInterval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "MetricsInterval" = member("day")
