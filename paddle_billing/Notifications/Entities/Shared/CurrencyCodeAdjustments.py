from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CurrencyCodeAdjustments(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    EUR: "CurrencyCodeAdjustments" = member("EUR")
    GBP: "CurrencyCodeAdjustments" = member("GBP")
    USD: "CurrencyCodeAdjustments" = member("USD")
