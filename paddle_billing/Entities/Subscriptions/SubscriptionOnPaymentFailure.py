from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionOnPaymentFailure(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PreventChange: "SubscriptionOnPaymentFailure" = member("prevent_change")
    ApplyChange: "SubscriptionOnPaymentFailure" = member("apply_change")
