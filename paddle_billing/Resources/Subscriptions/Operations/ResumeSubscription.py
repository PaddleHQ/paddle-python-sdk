from dataclasses import dataclass

from paddle_billing.Entities.DateTime      import DateTime
from paddle_billing.Entities.Subscriptions import SubscriptionEffectiveFrom


@dataclass
class ResumeSubscription:
    effective_from: SubscriptionEffectiveFrom | DateTime | None = None


    def get_parameters(self) -> dict:
        effective_from = self.effective_from.format() \
            if isinstance(self.effective_from, DateTime) \
            else self.effective_from

        return {'effective_from': effective_from}
