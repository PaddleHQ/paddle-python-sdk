from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Origin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Api: "Origin" = member("api")
    SubscriptionCharge: "Origin" = member("subscription_charge")
    SubscriptionPaymentMethodChange: "Origin" = member("subscription_payment_method_change")
    SubscriptionRecurring: "Origin" = member("subscription_recurring")
    SubscriptionUpdate: "Origin" = member("subscription_update")
    Web: "Origin" = member("web")
