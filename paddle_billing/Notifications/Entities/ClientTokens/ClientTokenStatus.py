from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ClientTokenStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "ClientTokenStatus" = "active"
    Revoked: "ClientTokenStatus" = "revoked"
