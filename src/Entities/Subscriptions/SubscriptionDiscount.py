from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional


@dataclass
class SubscriptionDiscount:
    id:       str
    startsAt: datetime
    endsAt:   Optional[datetime]


    @staticmethod
    def from_dict(data: dict) -> SubscriptionDiscount:
        return SubscriptionDiscount(
            id       = data['id'],
            startsAt = datetime.fromisoformat(data['starts_at']),
            endsAt   = datetime.fromisoformat(data['ends_at']) if 'ends_at' in data else None,
        )
