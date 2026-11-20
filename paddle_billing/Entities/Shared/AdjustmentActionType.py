from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class AdjustmentActionType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Full: "AdjustmentActionType" = member("full")
    Partial: "AdjustmentActionType" = member("partial")
