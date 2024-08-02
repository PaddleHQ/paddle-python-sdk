from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CurrencyCodeAdjustments(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    EUR = 'EUR'
    GBP = 'GBP'
    USD = 'USD'
