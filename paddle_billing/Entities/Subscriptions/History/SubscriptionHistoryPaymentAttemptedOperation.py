from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionHistoryPaymentAttemptedOperation(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionUpdate: "SubscriptionHistoryPaymentAttemptedOperation" = "subscription_update"
    SubscriptionOneOffCharge: "SubscriptionHistoryPaymentAttemptedOperation" = "subscription_one_off_charge"
    SubscriptionActivate: "SubscriptionHistoryPaymentAttemptedOperation" = "subscription_activate"
