from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionStatusFilterValue(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionStatusFilterValue" = member("active")
    Canceled: "SubscriptionStatusFilterValue" = member("canceled")
    PastDue: "SubscriptionStatusFilterValue" = member("past_due")
    Paused: "SubscriptionStatusFilterValue" = member("paused")
    Trialing: "SubscriptionStatusFilterValue" = member("trialing")
