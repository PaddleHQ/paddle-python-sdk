from enum import StrEnum


class SubscriptionStatus(StrEnum):
    Active   = 'active'
    Canceled = 'canceled'
    PastDue  = 'past_due'
    Paused   = 'paused'
    Trialing = 'trialing'
    Inactive = 'inactive'
