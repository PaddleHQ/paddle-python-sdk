from enum import StrEnum


class Origin(StrEnum):
    Api                             = 'api'
    SubscriptionCharge              = 'subscription_charge'
    SubscriptionPaymentMethodChange = 'subscription_payment_method_change'
    SubscriptionRecurring           = 'subscription_recurring'
    SubscriptionUpdate              = 'subscription_update'
    Web                             = 'web'
