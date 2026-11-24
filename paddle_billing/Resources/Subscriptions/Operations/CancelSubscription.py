from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Entities.Subscriptions import SubscriptionEffectiveFrom as SubscriptionEffectiveFrom


@dataclass
class CancelSubscription(Operation):
    effective_from: SubscriptionEffectiveFrom | None = None
