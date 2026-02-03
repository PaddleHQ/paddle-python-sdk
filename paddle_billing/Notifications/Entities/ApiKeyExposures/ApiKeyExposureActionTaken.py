from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ApiKeyExposureActionTaken(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Revoked: "ApiKeyExposureActionTaken" = "revoked"
    None_: "ApiKeyExposureActionTaken" = "none"
