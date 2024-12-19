from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Subscriptions import SubscriptionResumeEffectiveFrom, SubscriptionOnResume
from paddle_billing.Undefined import Undefined


@dataclass
class ResumeSubscription(Operation):
    effective_from: SubscriptionResumeEffectiveFrom | DateTime | None = None
    on_resume: SubscriptionOnResume | Undefined = Undefined()
