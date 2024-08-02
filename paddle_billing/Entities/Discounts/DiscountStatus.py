from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DiscountStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active   = 'active'
    Archived = 'archived'
    Expired  = 'expired'
    Used     = 'used'
