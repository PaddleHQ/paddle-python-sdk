from enum import StrEnum


class DiscountStatus(StrEnum):
    Active   = 'active'
    Archived = 'archived'
    Expired  = 'expired'
    Used     = 'used'
