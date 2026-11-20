from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DiscountMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Standard: "DiscountMode" = member("standard")
    Custom: "DiscountMode" = member("custom")
