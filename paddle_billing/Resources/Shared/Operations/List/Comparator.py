from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Comparator(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    LT  = 'LT'
    LTE = 'LTE'
    GT  = 'GT'
    GTE = 'GTE'
