from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionScheduledChangeAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Cancel: "SubscriptionScheduledChangeAction" = "cancel"
    Pause: "SubscriptionScheduledChangeAction" = "pause"
    Resume: "SubscriptionScheduledChangeAction" = "resume"
