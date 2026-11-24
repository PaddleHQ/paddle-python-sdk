from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ApiKeyStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "ApiKeyStatus" = member("active")
    Expired: "ApiKeyStatus" = member("expired")
    Revoked: "ApiKeyStatus" = member("revoked")
