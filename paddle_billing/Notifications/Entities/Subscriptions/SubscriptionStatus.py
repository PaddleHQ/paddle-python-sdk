from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionStatus" = member("active")
    Canceled: "SubscriptionStatus" = member("canceled")
    PastDue: "SubscriptionStatus" = member("past_due")
    Paused: "SubscriptionStatus" = member("paused")
    Trialing: "SubscriptionStatus" = member("trialing")
    Inactive: "SubscriptionStatus" = member("inactive")
