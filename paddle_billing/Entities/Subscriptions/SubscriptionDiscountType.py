from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionDiscountType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Recurring: "SubscriptionDiscountType" = member("recurring")
    OneOff: "SubscriptionDiscountType" = member("one-off")
