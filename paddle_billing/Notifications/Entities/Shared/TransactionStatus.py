from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TransactionStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Draft     = 'draft'
    Ready     = 'ready'
    Billed    = 'billed'
    Paid      = 'paid'
    Completed = 'completed'
    Canceled  = 'canceled'
    PastDue   = 'past_due'
