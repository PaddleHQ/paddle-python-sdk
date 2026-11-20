from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class NotificationOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Event: "NotificationOrigin" = member("event")
    Replay: "NotificationOrigin" = member("replay")
