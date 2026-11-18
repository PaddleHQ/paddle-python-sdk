# mypy: disable-error-code="assignment"
from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class AudienceOptIn(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Never: "AudienceOptIn" = "never"
    Choice: "AudienceOptIn" = "choice"
