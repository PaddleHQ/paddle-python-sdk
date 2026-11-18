from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DiscountStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "DiscountStatus" = member("active")
    Archived: "DiscountStatus" = member("archived")
    Expired: "DiscountStatus" = member("expired")
    Used: "DiscountStatus" = member("used")
