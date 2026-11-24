from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SavedPaymentMethodOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SavedDuringPurchase: "SavedPaymentMethodOrigin" = member("saved_during_purchase")
    Subscription: "SavedPaymentMethodOrigin" = member("subscription")
