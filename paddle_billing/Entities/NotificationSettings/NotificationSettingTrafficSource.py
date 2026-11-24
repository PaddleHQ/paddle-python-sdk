from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class NotificationSettingTrafficSource(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    All: "NotificationSettingTrafficSource" = member("all")
    Platform: "NotificationSettingTrafficSource" = member("platform")
    Simulation: "NotificationSettingTrafficSource" = member("simulation")
