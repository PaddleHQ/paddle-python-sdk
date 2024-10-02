from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "DiscountStatus" = "active"
    Archived: "DiscountStatus" = "archived"
    Expired: "DiscountStatus" = "expired"
    Used: "DiscountStatus" = "used"
