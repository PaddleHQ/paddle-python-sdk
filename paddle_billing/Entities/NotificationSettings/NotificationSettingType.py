from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class NotificationSettingType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Email: "NotificationSettingType" = member("email")
    Url: "NotificationSettingType" = member("url")
