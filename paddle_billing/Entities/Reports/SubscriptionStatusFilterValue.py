from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionStatusFilterValue(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionStatusFilterValue" = "active"
    Canceled: "SubscriptionStatusFilterValue" = "canceled"
    PastDue: "SubscriptionStatusFilterValue" = "past_due"
    Paused: "SubscriptionStatusFilterValue" = "paused"
    Trialing: "SubscriptionStatusFilterValue" = "trialing"
