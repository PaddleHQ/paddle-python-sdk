from enum import Enum


class ReportType(Enum):
    Pending = 'pending'
    Ready   = 'ready'
    Failed  = 'failed'
    Expired = 'expired'
