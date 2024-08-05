from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class PaymentAttemptStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Authorized              = 'authorized'
    AuthorizedFlagged       = 'authorized_flagged'
    Canceled                = 'canceled'
    Captured                = 'captured'
    Error                   = 'error'
    ActionRequired          = 'action_required'
    PendingNoActionRequired = 'pending_no_action_required'
    Created                 = 'created'
    Unknown                 = 'unknown'
