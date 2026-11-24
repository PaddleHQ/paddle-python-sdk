from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class MetricsFieldType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    String: "MetricsFieldType" = member("string")
    Integer: "MetricsFieldType" = member("integer")
    Decimal: "MetricsFieldType" = member("decimal")
    Currency: "MetricsFieldType" = member("currency")
