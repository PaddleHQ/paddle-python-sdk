from dataclasses import dataclass

from paddle_billing.Entities.Subscriptions.SubscriptionEffectiveFrom import (
    SubscriptionEffectiveFrom as SubscriptionEffectiveFrom,
)


@dataclass
class SubscriptionDiscount:
    id: str
    effective_from: SubscriptionEffectiveFrom
