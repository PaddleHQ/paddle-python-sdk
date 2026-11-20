from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class AdjustmentTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    External: "AdjustmentTaxMode" = member("external")
    Internal: "AdjustmentTaxMode" = member("internal")
