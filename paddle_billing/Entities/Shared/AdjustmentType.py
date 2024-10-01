from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AdjustmentType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Full: "AdjustmentType" = "full"
    Partial: "AdjustmentType" = "partial"
    Tax: "AdjustmentType" = "tax"
    Proration: "AdjustmentType" = "proration"
