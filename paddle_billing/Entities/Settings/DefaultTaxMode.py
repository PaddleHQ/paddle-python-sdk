from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DefaultTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Exclusive: "DefaultTaxMode" = member("exclusive")
    Inclusive: "DefaultTaxMode" = member("inclusive")
    Location: "DefaultTaxMode" = member("location")
