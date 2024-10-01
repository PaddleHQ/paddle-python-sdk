from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AdjustmentStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PendingApproval: "AdjustmentStatus" = "pending_approval"
    Approved: "AdjustmentStatus" = "approved"
    Rejected: "AdjustmentStatus" = "rejected"
    Reversed: "AdjustmentStatus" = "reversed"
