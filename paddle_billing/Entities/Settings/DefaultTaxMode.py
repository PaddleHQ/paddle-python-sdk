from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DefaultTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Exclusive: "DefaultTaxMode" = "exclusive"
    Inclusive: "DefaultTaxMode" = "inclusive"
    Location: "DefaultTaxMode" = "location"
