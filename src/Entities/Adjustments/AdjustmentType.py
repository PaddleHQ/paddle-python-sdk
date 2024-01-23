from enum import StrEnum


class AdjustmentType(StrEnum):
    Full      = 'full'
    Partial   = 'partial'
    Tax       = 'tax'
    Proration = 'proration'
