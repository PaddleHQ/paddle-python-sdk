from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class BalanceCurrencyCode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AUD: "BalanceCurrencyCode" = member("AUD")
    CAD: "BalanceCurrencyCode" = member("CAD")
    EUR: "BalanceCurrencyCode" = member("EUR")
    GBP: "BalanceCurrencyCode" = member("GBP")
    USD: "BalanceCurrencyCode" = member("USD")
