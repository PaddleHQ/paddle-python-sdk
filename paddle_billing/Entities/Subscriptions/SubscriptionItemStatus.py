from paddle_billing.PaddleStrEnum import PaddleStrEnum


class SubscriptionItemStatus(PaddleStrEnum):
    Active   = 'active'
    Inactive = 'inactive'
    Trialing = 'trialing'
