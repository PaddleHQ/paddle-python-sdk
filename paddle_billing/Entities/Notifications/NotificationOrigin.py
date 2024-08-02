from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationOrigin(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Event  = 'event'
    Replay = 'replay'
