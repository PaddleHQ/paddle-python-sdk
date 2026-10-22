from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CheckoutDomainStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PendingReview: "CheckoutDomainStatus" = "pending_review"
    Approved: "CheckoutDomainStatus" = "approved"
    Rejected: "CheckoutDomainStatus" = "rejected"
    InReview: "CheckoutDomainStatus" = "in_review"
    ActionRequired: "CheckoutDomainStatus" = "action_required"
