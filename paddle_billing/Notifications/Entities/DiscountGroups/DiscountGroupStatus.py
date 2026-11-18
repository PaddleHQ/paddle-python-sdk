from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DiscountGroupStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "DiscountGroupStatus" = member("active")
    Archived: "DiscountGroupStatus" = member("archived")
