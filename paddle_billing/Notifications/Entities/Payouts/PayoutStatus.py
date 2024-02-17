from paddle_billing.PaddleStrEnum import PaddleStrEnum


class PayoutStatus(PaddleStrEnum):
    Unpaid = 'unpaid'
    Paid   = 'paid'
