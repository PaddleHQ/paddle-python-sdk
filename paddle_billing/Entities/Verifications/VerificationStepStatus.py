from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class VerificationStepStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "VerificationStepStatus" = member("pending")
    InProgress: "VerificationStepStatus" = member("in_progress")
    InReview: "VerificationStepStatus" = member("in_review")
    ActionRequired: "VerificationStepStatus" = member("action_required")
    Completed: "VerificationStepStatus" = member("completed")
    Failed: "VerificationStepStatus" = member("failed")
    Canceled: "VerificationStepStatus" = member("canceled")
