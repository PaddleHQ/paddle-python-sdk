from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SavedPaymentMethodOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SavedDuringPurchase: "SavedPaymentMethodOrigin" = "saved_during_purchase"
    Subscription: "SavedPaymentMethodOrigin" = "subscription"
