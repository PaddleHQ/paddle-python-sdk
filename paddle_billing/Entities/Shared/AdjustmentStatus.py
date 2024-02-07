from enum import StrEnum


class AdjustmentStatus(StrEnum):
    PendingApproval = 'pending_approval'
    Approved        = 'approved'
    Rejected        = 'rejected'
    Reversed        = 'reversed'
