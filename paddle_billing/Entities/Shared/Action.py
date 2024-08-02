from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Action(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Credit            = 'credit'
    CreditReverse     = 'credit_reverse'
    Refund            = 'refund'
    Chargeback        = 'chargeback'
    ChargebackReverse = 'chargeback_reverse'
    ChargebackWarning = 'chargeback_warning'
