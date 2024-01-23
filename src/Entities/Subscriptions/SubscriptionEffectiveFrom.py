from enum import StrEnum


class SubscriptionEffectiveFrom(StrEnum):
    NextBillingPeriod = 'next_billing_period'
    Immediately       = 'immediately'
