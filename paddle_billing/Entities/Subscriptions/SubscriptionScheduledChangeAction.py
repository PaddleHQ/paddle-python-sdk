from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionScheduledChangeAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Cancel: "SubscriptionScheduledChangeAction" = member("cancel")
    Pause: "SubscriptionScheduledChangeAction" = member("pause")
    Resume: "SubscriptionScheduledChangeAction" = member("resume")
