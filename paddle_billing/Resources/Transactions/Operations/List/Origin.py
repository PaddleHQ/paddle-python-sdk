from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Origin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Api: "Origin" = "api"
    SubscriptionCharge: "Origin" = "subscription_charge"
    SubscriptionPaymentMethodChange: "Origin" = "subscription_payment_method_change"
    SubscriptionRecurring: "Origin" = "subscription_recurring"
    SubscriptionUpdate: "Origin" = "subscription_update"
    Web: "Origin" = "web"
