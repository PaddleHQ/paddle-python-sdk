from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Status(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Active: "Status" = member("active")
    Archived: "Status" = member("archived")
