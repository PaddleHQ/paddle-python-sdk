from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class VerificationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "VerificationStatus" = member("pending")
    InProgress: "VerificationStatus" = member("in_progress")
    InReview: "VerificationStatus" = member("in_review")
    ActionRequired: "VerificationStatus" = member("action_required")
    Completed: "VerificationStatus" = member("completed")
    Failed: "VerificationStatus" = member("failed")
    Canceled: "VerificationStatus" = member("canceled")
