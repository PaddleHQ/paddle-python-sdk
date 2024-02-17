from paddle_billing.PaddleStrEnum import PaddleStrEnum


class SubscriptionScheduledChangeAction(PaddleStrEnum):
    Cancel = 'cancel'
    Pause  = 'pause'
    Resume = 'resume'
