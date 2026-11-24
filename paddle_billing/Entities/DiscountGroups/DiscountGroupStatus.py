from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DiscountGroupStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "DiscountGroupStatus" = member("active")
    Archived: "DiscountGroupStatus" = member("archived")
