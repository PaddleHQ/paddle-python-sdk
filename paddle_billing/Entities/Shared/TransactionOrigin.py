from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TransactionOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Api: "TransactionOrigin" = "api"
    SubscriptionCharge: "TransactionOrigin" = "subscription_charge"
    SubscriptionPaymentMethodChange: "TransactionOrigin" = "subscription_payment_method_change"
    SubscriptionRecurring: "TransactionOrigin" = "subscription_recurring"
    SubscriptionUpdate: "TransactionOrigin" = "subscription_update"
    Web: "TransactionOrigin" = "web"
