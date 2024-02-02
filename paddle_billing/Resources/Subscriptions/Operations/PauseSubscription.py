from dataclasses import asdict, dataclass

from paddle_billing.Entities.DateTime      import DateTime
from paddle_billing.Entities.Subscriptions import SubscriptionEffectiveFrom


@dataclass
class PauseSubscription:
    effective_from: SubscriptionEffectiveFrom | None = None
    resume_at:      DateTime                  | None = None


    def get_parameters(self) -> dict:
        parameters = asdict(self)
        parameters['resume_at'] = self.resume_at.format() \
            if isinstance(self.resume_at, DateTime) \
            else self.resume_at

        return parameters
