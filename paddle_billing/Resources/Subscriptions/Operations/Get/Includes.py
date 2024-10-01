from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextTransaction: "Includes" = "next_transaction"
    RecurringTransactionDetails: "Includes" = "recurring_transaction_details"
