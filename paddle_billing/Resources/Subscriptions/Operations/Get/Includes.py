from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextTransaction             = 'next_transaction'
    RecurringTransactionDetails = 'recurring_transaction_details'
