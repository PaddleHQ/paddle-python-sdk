from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionScheduledChangeActionFilterValue(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Cancel: "SubscriptionScheduledChangeActionFilterValue" = member("cancel")
    Pause: "SubscriptionScheduledChangeActionFilterValue" = member("pause")
    Resume: "SubscriptionScheduledChangeActionFilterValue" = member("resume")
    NoChange: "SubscriptionScheduledChangeActionFilterValue" = member("none")
