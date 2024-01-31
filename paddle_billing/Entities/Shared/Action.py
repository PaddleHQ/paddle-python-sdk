from enum import StrEnum


class Action(StrEnum):
    Credit            = 'credit'
    CreditReverse     = 'credit_reverse'
    Refund            = 'refund'
    Chargeback        = 'chargeback'
    ChargebackReverse = 'chargeback_reverse'
    ChargebackWarning = 'chargeback_warning'
