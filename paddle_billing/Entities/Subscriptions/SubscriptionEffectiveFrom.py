from paddle_billing.PaddleStrEnum import PaddleStrEnum


class SubscriptionEffectiveFrom(PaddleStrEnum):
    NextBillingPeriod = 'next_billing_period'
    Immediately       = 'immediately'
