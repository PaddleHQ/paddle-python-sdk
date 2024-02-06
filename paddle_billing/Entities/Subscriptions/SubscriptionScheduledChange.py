from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Subscriptions.SubscriptionScheduledChangeAction import SubscriptionScheduledChangeAction


@dataclass
class SubscriptionScheduledChange:
    action:       SubscriptionScheduledChangeAction
    effective_at: datetime
    resume_at:    datetime | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionScheduledChange:
        return SubscriptionScheduledChange(
            action       = SubscriptionScheduledChangeAction(data['action']),
            effective_at = datetime.fromisoformat(data['effective_at']),
            resume_at    = datetime.fromisoformat(data['resume_at']) if data.get('resume_at') else None,
        )
