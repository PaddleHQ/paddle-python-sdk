from paddle_billing.PaddleStrEnum import PaddleStrEnum


class SubscriptionStatus(PaddleStrEnum):
    Active   = 'active'
    Canceled = 'canceled'
    PastDue  = 'past_due'
    Paused   = 'paused'
    Trialing = 'trialing'
    Inactive = 'inactive'
