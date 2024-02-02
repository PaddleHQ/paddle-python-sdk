from dataclasses import asdict, dataclass

from paddle_billing.Entities.Subscriptions import SubscriptionEffectiveFrom


@dataclass
class CancelSubscription:
    effective_from: SubscriptionEffectiveFrom = None


    def get_parameters(self) -> dict:
        return asdict(self)
