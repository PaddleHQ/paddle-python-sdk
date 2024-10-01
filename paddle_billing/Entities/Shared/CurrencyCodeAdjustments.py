from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CurrencyCodeAdjustments(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    EUR: "CurrencyCodeAdjustments" = "EUR"
    GBP: "CurrencyCodeAdjustments" = "GBP"
    USD: "CurrencyCodeAdjustments" = "USD"
