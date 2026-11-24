from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class NotificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    NotAttempted: "NotificationStatus" = member("not_attempted")
    NeedsRetry: "NotificationStatus" = member("needs_retry")
    Delivered: "NotificationStatus" = member("delivered")
    Failed: "NotificationStatus" = member("failed")
