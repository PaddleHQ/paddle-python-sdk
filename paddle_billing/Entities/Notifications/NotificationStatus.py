from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotAttempted = 'not_attempted'
    NeedsRetry   = 'needs_retry'
    Delivered    = 'delivered'
    Failed       = 'failed'
