from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ApiKeyExposureRiskLevel(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    High: "ApiKeyExposureRiskLevel" = member("high")
    Low: "ApiKeyExposureRiskLevel" = member("low")
