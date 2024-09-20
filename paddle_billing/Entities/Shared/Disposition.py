from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Disposition(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Attachment: "Attachment"   = 'attachment'
    Inline: "Inline" = 'inline'
