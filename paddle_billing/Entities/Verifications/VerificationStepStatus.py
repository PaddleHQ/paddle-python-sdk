from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class VerificationStepStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "VerificationStepStatus" = "pending"
    InProgress: "VerificationStepStatus" = "in_progress"
    InReview: "VerificationStepStatus" = "in_review"
    ActionRequired: "VerificationStepStatus" = "action_required"
    Completed: "VerificationStepStatus" = "completed"
    Failed: "VerificationStepStatus" = "failed"
    Canceled: "VerificationStepStatus" = "canceled"
