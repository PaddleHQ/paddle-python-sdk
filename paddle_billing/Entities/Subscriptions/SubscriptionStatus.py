from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionStatus" = "active"
    Canceled: "SubscriptionStatus" = "canceled"
    PastDue: "SubscriptionStatus" = "past_due"
    Paused: "SubscriptionStatus" = "paused"
    Trialing: "SubscriptionStatus" = "trialing"
    Inactive: "SubscriptionStatus" = "inactive"
