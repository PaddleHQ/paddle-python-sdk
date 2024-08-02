from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionProrationBillingMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ProratedImmediately       = 'prorated_immediately'
    ProratedNextBillingPeriod = 'prorated_next_billing_period'
    FullImmediately           = 'full_immediately'
    FullNextBillingPeriod     = 'full_next_billing_period'
    DoNotBill                 = 'do_not_bill'
