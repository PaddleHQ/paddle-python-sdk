from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AdjustmentTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    External: "AdjustmentTaxMode" = "external"
    Internal: "AdjustmentTaxMode" = "internal"
