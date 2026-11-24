from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionScheduledChangeAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Cancel: "SubscriptionScheduledChangeAction" = member("cancel")
    Pause: "SubscriptionScheduledChangeAction" = member("pause")
    Resume: "SubscriptionScheduledChangeAction" = member("resume")
