from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ClientTokenStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "ClientTokenStatus" = member("active")
    Revoked: "ClientTokenStatus" = member("revoked")
