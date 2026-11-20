from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class Disposition(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Attachment: "Disposition" = member("attachment")
    Inline: "Disposition" = member("inline")
