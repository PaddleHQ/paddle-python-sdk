from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class ApiKeyExposureActionTaken(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Revoked: "ApiKeyExposureActionTaken" = member("revoked")
    None_: "ApiKeyExposureActionTaken" = member("none")
