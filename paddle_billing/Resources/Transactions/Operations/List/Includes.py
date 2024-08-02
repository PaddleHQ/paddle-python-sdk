from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Address                 = 'address'
    Adjustment              = 'adjustment'
    AdjustmentsTotals       = 'adjustments_totals'
    AvailablePaymentMethods = 'available_payment_methods'
    Business                = 'business'
    Customer                = 'customer'
    Discount                = 'discount'
