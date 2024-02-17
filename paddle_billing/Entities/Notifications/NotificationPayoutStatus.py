from paddle_billing.PaddleStrEnum import PaddleStrEnum


class NotificationPayoutStatus(PaddleStrEnum):
    Unpaid = 'unpaid'
    Paid   = 'paid'
