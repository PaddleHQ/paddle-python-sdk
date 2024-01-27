from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.DateTime                                import DateTime
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom import SubscriptionEffectiveFrom


@dataclass
class ResumeSubscription:
    effective_from: SubscriptionEffectiveFrom | DateTime | None = None


    def __post_init__(self):
        if isinstance(self.effective_from, DateTime):
            self.effective_from = DateTime.from_datetime(self.effective_from)


    def get_parameters(self) -> dict:
        effective_from = self.effective_from.format() if isinstance(self.effective_from, DateTime) else self.effective_from

        return {'effective_from': effective_from}
