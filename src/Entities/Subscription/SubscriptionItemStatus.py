from enum import StrEnum


class SubscriptionItemStatus(StrEnum):
    Active   = 'active'
    Inactive = 'inactive'
    Trialing = 'trialing'
