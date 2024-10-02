from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionResultAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Credit: "SubscriptionResultAction" = "credit"
    Charge: "SubscriptionResultAction" = "charge"
