from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DefaultTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Exclusive: "DefaultTaxMode" = member("exclusive")
    Inclusive: "DefaultTaxMode" = member("inclusive")
    Location: "DefaultTaxMode" = member("location")
