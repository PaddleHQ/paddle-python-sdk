from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ApiKeyStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "ApiKeyStatus" = member("active")
    Expired: "ApiKeyStatus" = member("expired")
    Revoked: "ApiKeyStatus" = member("revoked")
