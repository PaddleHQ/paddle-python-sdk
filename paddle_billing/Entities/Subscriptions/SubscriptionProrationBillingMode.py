from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionProrationBillingMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ProratedImmediately: "SubscriptionProrationBillingMode" = member("prorated_immediately")
    ProratedNextBillingPeriod: "SubscriptionProrationBillingMode" = member("prorated_next_billing_period")
    FullImmediately: "SubscriptionProrationBillingMode" = member("full_immediately")
    FullNextBillingPeriod: "SubscriptionProrationBillingMode" = member("full_next_billing_period")
    DoNotBill: "SubscriptionProrationBillingMode" = member("do_not_bill")
