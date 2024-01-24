from enum import StrEnum


class ReportStatus(StrEnum):
    Pending = 'pending'
    Ready   = 'ready'
    Failed  = 'failed'
    Expired = 'expired'
