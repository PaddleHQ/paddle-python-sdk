from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CustomerPaymentMethodOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SavedDuringPurchase: "CustomerPaymentMethodOrigin" = "saved_during_purchase"
    Subscription: "CustomerPaymentMethodOrigin" = "subscription"
