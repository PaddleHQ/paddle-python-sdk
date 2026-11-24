from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ApiKeyExposureSource(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Github: "ApiKeyExposureSource" = member("github")
