from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TransactionStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Draft: "TransactionStatus" = "draft"
    Ready: "TransactionStatus" = "ready"
    Billed: "TransactionStatus" = "billed"
    Paid: "TransactionStatus" = "paid"
    Completed: "TransactionStatus" = "completed"
    Canceled: "TransactionStatus" = "canceled"
    PastDue: "TransactionStatus" = "past_due"
