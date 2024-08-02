from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TransactionOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Api                             = 'api'
    SubscriptionCharge              = 'subscription_charge'
    SubscriptionPaymentMethodChange = 'subscription_payment_method_change'
    SubscriptionRecurring           = 'subscription_recurring'
    SubscriptionUpdate              = 'subscription_update'
    Web                             = 'web'
