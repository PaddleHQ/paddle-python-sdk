from paddle_billing.PaddleStrEnum import PaddleStrEnum


class AdjustmentStatus(PaddleStrEnum):
    PendingApproval = 'pending_approval'
    Approved        = 'approved'
    Rejected        = 'rejected'
    Reversed        = 'reversed'
