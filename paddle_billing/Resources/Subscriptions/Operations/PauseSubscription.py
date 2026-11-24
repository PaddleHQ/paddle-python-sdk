from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Entities.DateTime import DateTime as DateTime
from paddle_billing.Entities.Subscriptions import (
    SubscriptionEffectiveFrom as SubscriptionEffectiveFrom,
    SubscriptionOnResume as SubscriptionOnResume,
)
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class PauseSubscription(Operation):
    effective_from: SubscriptionEffectiveFrom | None = None
    resume_at: DateTime | None = None
    on_resume: SubscriptionOnResume | Undefined = Undefined()
