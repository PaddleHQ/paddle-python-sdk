from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionItemStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionItemStatus" = member("active")
    Inactive: "SubscriptionItemStatus" = member("inactive")
    Trialing: "SubscriptionItemStatus" = member("trialing")
