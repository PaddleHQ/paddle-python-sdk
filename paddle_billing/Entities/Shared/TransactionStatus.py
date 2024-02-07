from enum import StrEnum


class TransactionStatus(StrEnum):
    Draft     = 'draft'
    Ready     = 'ready'
    Billed    = 'billed'
    Paid      = 'paid'
    Completed = 'completed'
    Canceled  = 'canceled'
    PastDue   = 'past_due'
