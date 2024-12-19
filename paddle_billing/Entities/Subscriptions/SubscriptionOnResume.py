from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionOnResume(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ContinueExistingBillingPeriod: "SubscriptionOnResume" = "continue_existing_billing_period"
    StartNewBillingPeriod: "SubscriptionOnResume" = "start_new_billing_period"
