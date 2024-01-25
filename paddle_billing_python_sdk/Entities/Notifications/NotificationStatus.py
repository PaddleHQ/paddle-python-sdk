from enum import StrEnum


class NotificationStatus(StrEnum):
    NotAttempted = 'not_attempted'
    NeedsRetry   = 'needs_retry'
    Delivered    = 'delivered'
    Failed       = 'failed'
