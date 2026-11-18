from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class NotificationPayoutStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Unpaid: "NotificationPayoutStatus" = member("unpaid")
    Paid: "NotificationPayoutStatus" = member("paid")
