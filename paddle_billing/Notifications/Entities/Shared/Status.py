from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class Status(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "Status" = member("active")
    Archived: "Status" = member("archived")
