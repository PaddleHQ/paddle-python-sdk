from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Includes(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Address: "Includes" = member("address")
    Adjustment: "Includes" = member("adjustment")
    AdjustmentsTotals: "Includes" = member("adjustments_totals")
    AvailablePaymentMethods: "Includes" = member("available_payment_methods")
    Business: "Includes" = member("business")
    Customer: "Includes" = member("customer")
    Discount: "Includes" = member("discount")
