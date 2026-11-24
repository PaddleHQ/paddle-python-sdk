from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class AudienceOptIn(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Never: "AudienceOptIn" = member("never")
    Choice: "AudienceOptIn" = member("choice")
