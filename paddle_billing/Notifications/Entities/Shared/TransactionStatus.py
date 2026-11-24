from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class TransactionStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Draft: "TransactionStatus" = member("draft")
    Ready: "TransactionStatus" = member("ready")
    Billed: "TransactionStatus" = member("billed")
    Paid: "TransactionStatus" = member("paid")
    Completed: "TransactionStatus" = member("completed")
    Canceled: "TransactionStatus" = member("canceled")
    PastDue: "TransactionStatus" = member("past_due")
