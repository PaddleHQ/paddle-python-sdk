from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime


@dataclass
class SubscriptionDiscount:
    id:        str
    starts_at: datetime
    ends_at:   datetime


    @staticmethod
    def from_dict(data: dict) -> SubscriptionDiscount:
        return SubscriptionDiscount(
            id        = data['id'],
            starts_at = datetime.fromisoformat(data['starts_at']),
            ends_at   = datetime.fromisoformat(data['ends_at']) if data.get('ends_at') else None,
        )
