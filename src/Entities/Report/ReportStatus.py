from enum import StrEnum


class ReportType(StrEnum):
    Pending = 'pending'
    Ready   = 'ready'
    Failed  = 'failed'
    Expired = 'expired'
