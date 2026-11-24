from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class BalanceCurrencyCode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AUD: "BalanceCurrencyCode" = member("AUD")
    CAD: "BalanceCurrencyCode" = member("CAD")
    EUR: "BalanceCurrencyCode" = member("EUR")
    GBP: "BalanceCurrencyCode" = member("GBP")
    USD: "BalanceCurrencyCode" = member("USD")
