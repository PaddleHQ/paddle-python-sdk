from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Entities.Subscriptions import SubscriptionEffectiveFrom


@dataclass
class CancelSubscription(Operation):
    effective_from: SubscriptionEffectiveFrom = None
