from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DiscountInclude(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    DiscountGroup: "DiscountInclude" = member("discount_group")
