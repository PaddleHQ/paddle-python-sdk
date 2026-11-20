from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ApiKeyExposureRiskLevel(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    High: "ApiKeyExposureRiskLevel" = member("high")
    Low: "ApiKeyExposureRiskLevel" = member("low")
