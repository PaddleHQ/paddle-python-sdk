from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CheckoutDomainStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PendingReview: "CheckoutDomainStatus" = member("pending_review")
    Approved: "CheckoutDomainStatus" = member("approved")
    Rejected: "CheckoutDomainStatus" = member("rejected")
    InReview: "CheckoutDomainStatus" = member("in_review")
    ActionRequired: "CheckoutDomainStatus" = member("action_required")
