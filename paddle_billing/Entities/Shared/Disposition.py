from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Disposition(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Attachment: "Disposition" = member("attachment")
    Inline: "Disposition" = member("inline")
