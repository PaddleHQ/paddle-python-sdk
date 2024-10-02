from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotAttempted: "NotificationStatus" = "not_attempted"
    NeedsRetry: "NotificationStatus" = "needs_retry"
    Delivered: "NotificationStatus" = "delivered"
    Failed: "NotificationStatus" = "failed"
