from dataclasses import asdict, dataclass

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom import SubscriptionEffectiveFrom


@dataclass
class CancelSubscription:
    effective_from: SubscriptionEffectiveFrom = None


    def get_parameters(self) -> dict:
        return asdict(self)
