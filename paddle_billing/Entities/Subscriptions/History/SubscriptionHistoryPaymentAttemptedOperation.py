from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionHistoryPaymentAttemptedOperation(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionUpdate: "SubscriptionHistoryPaymentAttemptedOperation" = member("subscription_update")
    SubscriptionOneOffCharge: "SubscriptionHistoryPaymentAttemptedOperation" = member("subscription_one_off_charge")
    SubscriptionActivate: "SubscriptionHistoryPaymentAttemptedOperation" = member("subscription_activate")
