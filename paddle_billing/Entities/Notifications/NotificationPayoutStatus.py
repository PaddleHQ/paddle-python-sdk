from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class NotificationPayoutStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Unpaid: "NotificationPayoutStatus" = member("unpaid")
    Paid: "NotificationPayoutStatus" = member("paid")
