from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending = 'pending'
    Ready   = 'ready'
    Failed  = 'failed'
    Expired = 'expired'
