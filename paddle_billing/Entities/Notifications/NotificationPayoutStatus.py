from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationPayoutStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Unpaid: "NotificationPayoutStatus" = "unpaid"
    Paid: "NotificationPayoutStatus" = "paid"
