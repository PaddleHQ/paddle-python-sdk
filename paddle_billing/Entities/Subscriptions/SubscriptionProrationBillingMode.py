from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionProrationBillingMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ProratedImmediately: "SubscriptionProrationBillingMode" = "prorated_immediately"
    ProratedNextBillingPeriod: "SubscriptionProrationBillingMode" = "prorated_next_billing_period"
    FullImmediately: "SubscriptionProrationBillingMode" = "full_immediately"
    FullNextBillingPeriod: "SubscriptionProrationBillingMode" = "full_next_billing_period"
    DoNotBill: "SubscriptionProrationBillingMode" = "do_not_bill"
