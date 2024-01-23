from enum import StrEnum


class SubscriptionScheduledChangeAction(StrEnum):
    Cancel = 'cancel'
    Pause = 'pause'
    Resume = 'resume'
