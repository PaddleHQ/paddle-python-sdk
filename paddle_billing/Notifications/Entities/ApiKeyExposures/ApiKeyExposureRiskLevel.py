from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ApiKeyExposureRiskLevel(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    High: "ApiKeyExposureRiskLevel" = "high"
    Low: "ApiKeyExposureRiskLevel" = "low"
