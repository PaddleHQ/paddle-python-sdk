from paddle_billing.PaddleStrEnum import PaddleStrEnum


class DiscountStatus(PaddleStrEnum):
    Active   = 'active'
    Archived = 'archived'
    Expired  = 'expired'
    Used     = 'used'
