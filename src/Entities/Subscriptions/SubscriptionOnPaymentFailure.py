from enum import StrEnum


class SubscriptionOnPaymentFailure(StrEnum):
    PreventChange = 'prevent_change'
    ApplyChange   = 'apply_change'
