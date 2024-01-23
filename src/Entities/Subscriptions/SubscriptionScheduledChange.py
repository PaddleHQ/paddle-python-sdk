from __future__                         import annotations
from .SubscriptionScheduledChangeAction import SubscriptionScheduledChangeAction
from dataclasses                        import dataclass
from datetime                           import datetime
from typing                             import Optional


@dataclass
class SubscriptionScheduledChange:
    action:      SubscriptionScheduledChangeAction
    effectiveAt: datetime
    resumeAt:    Optional[datetime]


    @staticmethod
    def from_dict(data: dict) -> SubscriptionScheduledChange:
        return SubscriptionScheduledChange(
            action      = SubscriptionScheduledChangeAction(data['action']),
            effectiveAt = datetime.fromisoformat(data['effective_at']),
            resumeAt    = datetime.fromisoformat(data['resume_at']) if 'resume_at' in data else None,
        )
