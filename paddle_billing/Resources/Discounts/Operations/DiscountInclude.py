from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountInclude(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    DiscountGroup: "DiscountInclude" = "discount_group"
