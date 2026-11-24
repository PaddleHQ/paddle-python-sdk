from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class DunningExhaustedAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionPaused: "DunningExhaustedAction" = member("subscription_paused")
    SubscriptionCanceled: "DunningExhaustedAction" = member("subscription_canceled")
