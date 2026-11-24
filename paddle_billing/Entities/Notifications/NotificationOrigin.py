from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class NotificationOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Event: "NotificationOrigin" = member("event")
    Replay: "NotificationOrigin" = member("replay")
