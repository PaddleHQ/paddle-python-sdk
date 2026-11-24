from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CurrencyCodePayouts(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AUD: "CurrencyCodePayouts" = member("AUD")
    CAD: "CurrencyCodePayouts" = member("CAD")
    CHF: "CurrencyCodePayouts" = member("CHF")
    CNY: "CurrencyCodePayouts" = member("CNY")
    CZK: "CurrencyCodePayouts" = member("CZK")
    DKK: "CurrencyCodePayouts" = member("DKK")
    EUR: "CurrencyCodePayouts" = member("EUR")
    GBP: "CurrencyCodePayouts" = member("GBP")
    HUF: "CurrencyCodePayouts" = member("HUF")
    PLN: "CurrencyCodePayouts" = member("PLN")
    SEK: "CurrencyCodePayouts" = member("SEK")
    USD: "CurrencyCodePayouts" = member("USD")
    ZAR: "CurrencyCodePayouts" = member("ZAR")
