from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class AdjustmentTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    External: "AdjustmentTaxMode" = member("external")
    Internal: "AdjustmentTaxMode" = member("internal")
