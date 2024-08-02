from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationSettingType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Email = 'email'
    Url   = 'url'
