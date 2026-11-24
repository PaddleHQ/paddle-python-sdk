from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ApiKeyExposureSource(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Github: "ApiKeyExposureSource" = member("github")
