from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active   = 'active'
    Canceled = 'canceled'
    PastDue  = 'past_due'
    Paused   = 'paused'
    Trialing = 'trialing'
    Inactive = 'inactive'
