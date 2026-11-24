from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionOnPaymentFailure(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PreventChange: "SubscriptionOnPaymentFailure" = member("prevent_change")
    ApplyChange: "SubscriptionOnPaymentFailure" = member("apply_change")
