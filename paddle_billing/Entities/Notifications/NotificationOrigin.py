from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Event: "NotificationOrigin" = "event"
    Replay: "NotificationOrigin" = "replay"
