from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class PayoutStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Unpaid: "PayoutStatus" = "unpaid"
    Paid: "PayoutStatus" = "paid"
