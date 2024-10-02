from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Disposition(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Attachment: "Disposition" = "attachment"
    Inline: "Disposition" = "inline"
