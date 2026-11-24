from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class PaymentAttemptStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Authorized: "PaymentAttemptStatus" = member("authorized")
    AuthorizedFlagged: "PaymentAttemptStatus" = member("authorized_flagged")
    Canceled: "PaymentAttemptStatus" = member("canceled")
    Captured: "PaymentAttemptStatus" = member("captured")
    Error: "PaymentAttemptStatus" = member("error")
    ActionRequired: "PaymentAttemptStatus" = member("action_required")
    PendingNoActionRequired: "PaymentAttemptStatus" = member("pending_no_action_required")
    Created: "PaymentAttemptStatus" = member("created")
    Unknown: "PaymentAttemptStatus" = member("unknown")
    Dropped: "PaymentAttemptStatus" = member("dropped")
