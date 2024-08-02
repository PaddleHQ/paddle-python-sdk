from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AdjustmentStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PendingApproval = 'pending_approval'
    Approved        = 'approved'
    Rejected        = 'rejected'
    Reversed        = 'reversed'
