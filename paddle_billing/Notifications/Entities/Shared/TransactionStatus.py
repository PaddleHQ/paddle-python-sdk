from paddle_billing.PaddleStrEnum import PaddleStrEnum


class TransactionStatus(PaddleStrEnum):
    Draft     = 'draft'
    Ready     = 'ready'
    Billed    = 'billed'
    Paid      = 'paid'
    Completed = 'completed'
    Canceled  = 'canceled'
    PastDue   = 'past_due'
