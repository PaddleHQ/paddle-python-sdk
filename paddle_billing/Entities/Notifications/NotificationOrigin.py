from paddle_billing.PaddleStrEnum import PaddleStrEnum


class NotificationOrigin(PaddleStrEnum):
    Event  = 'event'
    Replay = 'replay'
