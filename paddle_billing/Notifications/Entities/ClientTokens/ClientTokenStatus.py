from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ClientTokenStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "ClientTokenStatus" = member("active")
    Revoked: "ClientTokenStatus" = member("revoked")
