from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SavedPaymentMethodOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SavedDuringPurchase: "SavedPaymentMethodOrigin" = member("saved_during_purchase")
    Subscription: "SavedPaymentMethodOrigin" = member("subscription")
