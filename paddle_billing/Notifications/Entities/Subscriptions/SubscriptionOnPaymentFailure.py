from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionOnPaymentFailure(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PreventChange: "SubscriptionOnPaymentFailure" = "prevent_change"
    ApplyChange: "SubscriptionOnPaymentFailure" = "apply_change"
