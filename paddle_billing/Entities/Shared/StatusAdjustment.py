from enum import StrEnum


class StatusAdjustment(StrEnum):
    PendingApproval = 'pending_approval'
    Approved        = 'approved'
    Rejected        = 'rejected'
    Reversed        = 'reversed'
