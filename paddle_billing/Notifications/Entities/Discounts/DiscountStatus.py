from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DiscountStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "DiscountStatus" = member("active")
    Archived: "DiscountStatus" = member("archived")
    Expired: "DiscountStatus" = member("expired")
    Used: "DiscountStatus" = member("used")
