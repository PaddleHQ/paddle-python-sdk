from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class NotificationSettingType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Email: "NotificationSettingType" = member("email")
    Url: "NotificationSettingType" = member("url")
