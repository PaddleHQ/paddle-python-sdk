from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ApiKeyRotationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "ApiKeyRotationStatus" = member("pending")
    Completed: "ApiKeyRotationStatus" = member("completed")
    Canceled: "ApiKeyRotationStatus" = member("canceled")
    Expired: "ApiKeyRotationStatus" = member("expired")
