from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class NotificationSettingTrafficSource(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    All: "NotificationSettingTrafficSource" = "all"
    Platform: "NotificationSettingTrafficSource" = "platform"
    Simulation: "NotificationSettingTrafficSource" = "simulation"
