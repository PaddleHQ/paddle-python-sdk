from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DiscountMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Standard: "DiscountMode" = member("standard")
    Custom: "DiscountMode" = member("custom")
