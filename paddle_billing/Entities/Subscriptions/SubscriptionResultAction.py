from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class SubscriptionResultAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Credit: "SubscriptionResultAction" = member("credit")
    Charge: "SubscriptionResultAction" = member("charge")
