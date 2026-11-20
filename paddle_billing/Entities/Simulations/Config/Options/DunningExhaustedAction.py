from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class DunningExhaustedAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionPaused: "DunningExhaustedAction" = member("subscription_paused")
    SubscriptionCanceled: "DunningExhaustedAction" = member("subscription_canceled")
