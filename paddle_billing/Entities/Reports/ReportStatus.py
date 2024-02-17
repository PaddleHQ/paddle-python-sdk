from paddle_billing.PaddleStrEnum import PaddleStrEnum


class ReportStatus(PaddleStrEnum):
    Pending = 'pending'
    Ready   = 'ready'
    Failed  = 'failed'
    Expired = 'expired'
