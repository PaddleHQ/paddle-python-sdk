from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionDiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Recurring: "SubscriptionDiscountType" = "recurring"
    OneOff: "SubscriptionDiscountType" = "one-off"
