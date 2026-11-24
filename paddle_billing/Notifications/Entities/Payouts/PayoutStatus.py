from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class PayoutStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Unpaid: "PayoutStatus" = member("unpaid")
    Paid: "PayoutStatus" = member("paid")
