from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Subscriptions import SubscriptionEffectiveFrom, SubscriptionOnResume
from paddle_billing.Undefined import Undefined


@dataclass
class PauseSubscription(Operation):
    effective_from: SubscriptionEffectiveFrom | None = None
    resume_at: DateTime | None = None
    on_resume: SubscriptionOnResume | Undefined = Undefined()
