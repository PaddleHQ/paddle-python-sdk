from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CurrencyCodePayouts(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AUD = 'AUD'
    CAD = 'CAD'
    CHF = 'CHF'
    CNY = 'CNY'
    CZK = 'CZK'
    DKK = 'DKK'
    EUR = 'EUR'
    GBP = 'GBP'
    HUF = 'HUF'
    PLN = 'PLN'
    SEK = 'SEK'
    USD = 'USD'
    ZAR = 'ZAR'
