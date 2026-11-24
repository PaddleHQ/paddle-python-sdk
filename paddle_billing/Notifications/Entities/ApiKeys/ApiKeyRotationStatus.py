from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ApiKeyRotationStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "ApiKeyRotationStatus" = member("pending")
    Completed: "ApiKeyRotationStatus" = member("completed")
    Canceled: "ApiKeyRotationStatus" = member("canceled")
    Expired: "ApiKeyRotationStatus" = member("expired")
