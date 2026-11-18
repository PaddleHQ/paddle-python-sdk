# mypy: disable-error-code="assignment"
from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ApiKeyExposureSource(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Github: "ApiKeyExposureSource" = "github"
