from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Address: "Includes" = "address"
    Adjustment: "Includes" = "adjustment"
    AdjustmentsTotals: "Includes" = "adjustments_totals"
    AvailablePaymentMethods: "Includes" = "available_payment_methods"
    Business: "Includes" = "business"
    Customer: "Includes" = "customer"
    Discount: "Includes" = "discount"
