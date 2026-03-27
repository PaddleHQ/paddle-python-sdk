from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class MetricsInterval(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Day: "MetricsInterval" = "day"
