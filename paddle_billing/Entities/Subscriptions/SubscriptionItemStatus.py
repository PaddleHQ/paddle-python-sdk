from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionItemStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionItemStatus" = member("active")
    Inactive: "SubscriptionItemStatus" = member("inactive")
    Trialing: "SubscriptionItemStatus" = member("trialing")
