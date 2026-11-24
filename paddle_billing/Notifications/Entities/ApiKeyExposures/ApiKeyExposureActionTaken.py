from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ApiKeyExposureActionTaken(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Revoked: "ApiKeyExposureActionTaken" = member("revoked")
    None_: "ApiKeyExposureActionTaken" = member("none")
