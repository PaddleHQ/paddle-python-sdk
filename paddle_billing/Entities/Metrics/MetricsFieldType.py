from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class MetricsFieldType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    String: "MetricsFieldType" = member("string")
    Integer: "MetricsFieldType" = member("integer")
    Decimal: "MetricsFieldType" = member("decimal")
    Currency: "MetricsFieldType" = member("currency")
