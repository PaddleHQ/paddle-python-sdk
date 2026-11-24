from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Entities.DateTime import DateTime as DateTime
from paddle_billing.Entities.Subscriptions import (
    SubscriptionResumeEffectiveFrom as SubscriptionResumeEffectiveFrom,
    SubscriptionOnResume as SubscriptionOnResume,
)
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class ResumeSubscription(Operation):
    effective_from: SubscriptionResumeEffectiveFrom | DateTime | None = None
    on_resume: SubscriptionOnResume | Undefined = Undefined()
