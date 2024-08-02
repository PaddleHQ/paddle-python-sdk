from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AdjustmentType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Full      = 'full'
    Partial   = 'partial'
    Tax       = 'tax'
    Proration = 'proration'
