from paddle_billing.PaddleStrEnum import PaddleStrEnum


class SubscriptionOnPaymentFailure(PaddleStrEnum):
    PreventChange = 'prevent_change'
    ApplyChange   = 'apply_change'
