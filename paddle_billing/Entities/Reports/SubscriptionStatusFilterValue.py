from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionStatusFilterValue(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionStatusFilterValue" = member("active")
    Canceled: "SubscriptionStatusFilterValue" = member("canceled")
    PastDue: "SubscriptionStatusFilterValue" = member("past_due")
    Paused: "SubscriptionStatusFilterValue" = member("paused")
    Trialing: "SubscriptionStatusFilterValue" = member("trialing")
