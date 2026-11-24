from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class MetricsFilterOperator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    In: "MetricsFilterOperator" = member("in")
