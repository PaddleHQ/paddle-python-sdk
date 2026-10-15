from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionScheduledChangeActionFilterValue(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Cancel: "SubscriptionScheduledChangeActionFilterValue" = "cancel"
    Pause: "SubscriptionScheduledChangeActionFilterValue" = "pause"
    Resume: "SubscriptionScheduledChangeActionFilterValue" = "resume"
    NoChange: "SubscriptionScheduledChangeActionFilterValue" = "none"
