from paddle_billing.PaddleStrEnum import PaddleStrEnum


class AdjustmentType(PaddleStrEnum):
    Full      = 'full'
    Partial   = 'partial'
    Tax       = 'tax'
    Proration = 'proration'
