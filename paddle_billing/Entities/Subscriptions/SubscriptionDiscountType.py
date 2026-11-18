from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionDiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Recurring: "SubscriptionDiscountType" = member("recurring")
    OneOff: "SubscriptionDiscountType" = member("one-off")
