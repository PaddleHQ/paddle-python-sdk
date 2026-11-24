from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NextTransaction: "Includes" = member("next_transaction")
    RecurringTransactionDetails: "Includes" = member("recurring_transaction_details")
