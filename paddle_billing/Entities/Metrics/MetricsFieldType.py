from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class MetricsFieldType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    String: "MetricsFieldType" = "string"
    Integer: "MetricsFieldType" = "integer"
    Decimal: "MetricsFieldType" = "decimal"
    Currency: "MetricsFieldType" = "currency"
