from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class PaymentAttemptStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Authorized: "PaymentAttemptStatus" = "authorized"
    AuthorizedFlagged: "PaymentAttemptStatus" = "authorized_flagged"
    Canceled: "PaymentAttemptStatus" = "canceled"
    Captured: "PaymentAttemptStatus" = "captured"
    Error: "PaymentAttemptStatus" = "error"
    ActionRequired: "PaymentAttemptStatus" = "action_required"
    PendingNoActionRequired: "PaymentAttemptStatus" = "pending_no_action_required"
    Created: "PaymentAttemptStatus" = "created"
    Unknown: "PaymentAttemptStatus" = "unknown"
