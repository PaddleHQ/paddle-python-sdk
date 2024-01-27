from dataclasses import asdict, dataclass

from paddle_billing_python_sdk.Entities.DateTime                                import DateTime
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom import SubscriptionEffectiveFrom


@dataclass
class PauseSubscription:
    effective_from: SubscriptionEffectiveFrom | None = None
    resume_at:      DateTime                  | None = None


    def get_parameters(self) -> dict:
        return asdict(self)
