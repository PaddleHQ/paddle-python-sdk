from paddle_billing.PaddleStrEnum import PaddleStrEnum


class Origin(PaddleStrEnum):
    Api                             = 'api'
    SubscriptionCharge              = 'subscription_charge'
    SubscriptionPaymentMethodChange = 'subscription_payment_method_change'
    SubscriptionRecurring           = 'subscription_recurring'
    SubscriptionUpdate              = 'subscription_update'
    Web                             = 'web'
