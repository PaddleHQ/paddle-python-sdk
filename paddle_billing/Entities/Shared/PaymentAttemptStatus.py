from enum import StrEnum


class PaymentAttemptStatus(StrEnum):
    Authorized              = 'authorized'
    AuthorizedFlagged       = 'authorized_flagged'
    Canceled                = 'canceled'
    Captured                = 'captured'
    Error                   = 'error'
    ActionRequired          = 'action_required'
    PendingNoActionRequired = 'pending_no_action_required'
    Created                 = 'created'
    Unknown                 = 'unknown'
