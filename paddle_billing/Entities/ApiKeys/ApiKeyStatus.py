from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ApiKeyStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "ApiKeyStatus" = "active"
    Expired: "ApiKeyStatus" = "expired"
    Revoked: "ApiKeyStatus" = "revoked"
