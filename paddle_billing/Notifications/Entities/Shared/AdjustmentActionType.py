from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class AdjustmentActionType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Full: "AdjustmentActionType" = member("full")
    Partial: "AdjustmentActionType" = member("partial")
