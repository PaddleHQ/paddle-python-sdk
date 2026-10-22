from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class VerificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "VerificationStatus" = "pending"
    InProgress: "VerificationStatus" = "in_progress"
    InReview: "VerificationStatus" = "in_review"
    ActionRequired: "VerificationStatus" = "action_required"
    Completed: "VerificationStatus" = "completed"
    Failed: "VerificationStatus" = "failed"
    Canceled: "VerificationStatus" = "canceled"
