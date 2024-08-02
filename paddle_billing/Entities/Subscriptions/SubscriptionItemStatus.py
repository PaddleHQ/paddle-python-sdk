from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionItemStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active   = 'active'
    Inactive = 'inactive'
    Trialing = 'trialing'
