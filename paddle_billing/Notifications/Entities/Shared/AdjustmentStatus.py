from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class AdjustmentStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PendingApproval: "AdjustmentStatus" = member("pending_approval")
    Approved: "AdjustmentStatus" = member("approved")
    Rejected: "AdjustmentStatus" = member("rejected")
    Reversed: "AdjustmentStatus" = member("reversed")
