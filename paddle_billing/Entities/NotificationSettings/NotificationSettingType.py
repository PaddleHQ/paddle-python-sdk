# mypy: disable-error-code="assignment"
from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationSettingType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Email: "NotificationSettingType" = "email"
    Url: "NotificationSettingType" = "url"
