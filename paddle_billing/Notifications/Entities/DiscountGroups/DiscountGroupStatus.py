from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountGroupStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "DiscountGroupStatus" = "active"
    Archived: "DiscountGroupStatus" = "archived"
