from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AdjustmentActionType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Full: "AdjustmentActionType" = "full"
    Partial: "AdjustmentActionType" = "partial"
