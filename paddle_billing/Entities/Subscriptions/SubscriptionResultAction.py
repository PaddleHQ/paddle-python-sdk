from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class SubscriptionResultAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Credit: "SubscriptionResultAction" = member("credit")
    Charge: "SubscriptionResultAction" = member("charge")
