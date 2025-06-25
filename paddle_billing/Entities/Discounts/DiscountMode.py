from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Standard: "DiscountMode" = "standard"
    Custom: "DiscountMode" = "custom"
