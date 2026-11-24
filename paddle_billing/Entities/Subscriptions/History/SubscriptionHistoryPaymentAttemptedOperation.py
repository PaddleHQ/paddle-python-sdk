from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionHistoryPaymentAttemptedOperation(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionUpdate: "SubscriptionHistoryPaymentAttemptedOperation" = member("subscription_update")
    SubscriptionOneOffCharge: "SubscriptionHistoryPaymentAttemptedOperation" = member("subscription_one_off_charge")
    SubscriptionActivate: "SubscriptionHistoryPaymentAttemptedOperation" = member("subscription_activate")
