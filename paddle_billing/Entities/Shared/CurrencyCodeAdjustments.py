from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class CurrencyCodeAdjustments(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    EUR: "CurrencyCodeAdjustments" = member("EUR")
    GBP: "CurrencyCodeAdjustments" = member("GBP")
    USD: "CurrencyCodeAdjustments" = member("USD")
