from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class TransactionOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Api: "TransactionOrigin" = member("api")
    SubscriptionCharge: "TransactionOrigin" = member("subscription_charge")
    SubscriptionPaymentMethodChange: "TransactionOrigin" = member("subscription_payment_method_change")
    SubscriptionRecurring: "TransactionOrigin" = member("subscription_recurring")
    SubscriptionUpdate: "TransactionOrigin" = member("subscription_update")
    Web: "TransactionOrigin" = member("web")
