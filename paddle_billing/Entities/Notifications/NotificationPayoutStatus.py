from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationPayoutStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Unpaid = 'unpaid'
    Paid   = 'paid'
