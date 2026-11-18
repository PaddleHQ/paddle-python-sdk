from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextTransaction: "Includes" = member("next_transaction")
    RecurringTransactionDetails: "Includes" = member("recurring_transaction_details")
