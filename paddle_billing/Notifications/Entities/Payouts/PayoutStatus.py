from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class PayoutStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Unpaid: "PayoutStatus" = member("unpaid")
    Paid: "PayoutStatus" = member("paid")
