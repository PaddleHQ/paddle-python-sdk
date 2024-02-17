from paddle_billing.PaddleStrEnum import PaddleStrEnum


class Action(PaddleStrEnum):
    Credit            = 'credit'
    CreditReverse     = 'credit_reverse'
    Refund            = 'refund'
    Chargeback        = 'chargeback'
    ChargebackReverse = 'chargeback_reverse'
    ChargebackWarning = 'chargeback_warning'
