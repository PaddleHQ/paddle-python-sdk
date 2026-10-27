from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class BalanceCurrencyCode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AUD: "BalanceCurrencyCode" = "AUD"
    CAD: "BalanceCurrencyCode" = "CAD"
    EUR: "BalanceCurrencyCode" = "EUR"
    GBP: "BalanceCurrencyCode" = "GBP"
    USD: "BalanceCurrencyCode" = "USD"
