from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionOnPaymentFailure(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PreventChange = 'prevent_change'
    ApplyChange   = 'apply_change'
