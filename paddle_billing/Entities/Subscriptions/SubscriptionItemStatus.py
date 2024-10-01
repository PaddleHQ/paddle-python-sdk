from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionItemStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "SubscriptionItemStatus" = "active"
    Inactive: "SubscriptionItemStatus" = "inactive"
    Trialing: "SubscriptionItemStatus" = "trialing"
