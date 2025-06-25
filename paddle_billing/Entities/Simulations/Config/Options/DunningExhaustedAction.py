from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class DunningExhaustedAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    SubscriptionPaused: "DunningExhaustedAction" = "subscription_paused"
    SubscriptionCanceled: "DunningExhaustedAction" = "subscription_canceled"
