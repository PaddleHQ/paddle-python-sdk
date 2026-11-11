from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ApiKeyRotationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "ApiKeyRotationStatus" = "pending"
    Completed: "ApiKeyRotationStatus" = "completed"
    Canceled: "ApiKeyRotationStatus" = "canceled"
    Expired: "ApiKeyRotationStatus" = "expired"
