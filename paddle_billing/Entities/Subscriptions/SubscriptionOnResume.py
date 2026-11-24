from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionOnResume(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ContinueExistingBillingPeriod: "SubscriptionOnResume" = member("continue_existing_billing_period")
    StartNewBillingPeriod: "SubscriptionOnResume" = member("start_new_billing_period")
