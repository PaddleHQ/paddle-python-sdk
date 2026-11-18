from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class AdjustmentType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Full: "AdjustmentType" = member("full")
    Partial: "AdjustmentType" = member("partial")
    Tax: "AdjustmentType" = member("tax")
    Proration: "AdjustmentType" = member("proration")
