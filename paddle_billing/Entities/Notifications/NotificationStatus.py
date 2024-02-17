from paddle_billing.PaddleStrEnum import PaddleStrEnum


class NotificationStatus(PaddleStrEnum):
    NotAttempted = 'not_attempted'
    NeedsRetry   = 'needs_retry'
    Delivered    = 'delivered'
    Failed       = 'failed'
