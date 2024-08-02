from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class SubscriptionScheduledChangeAction(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Cancel = 'cancel'
    Pause  = 'pause'
    Resume = 'resume'
