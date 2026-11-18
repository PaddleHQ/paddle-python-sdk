from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DiscountInclude(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    DiscountGroup: "DiscountInclude" = member("discount_group")
