from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass
class SubscriptionDiscount:
    id: str
    starts_at: datetime | None
    ends_at: datetime | None

    @staticmethod
    def from_dict(data: dict) -> SubscriptionDiscount:
        return SubscriptionDiscount(
            id=data["id"],
            starts_at=datetime.fromisoformat(data["starts_at"]) if data.get("starts_at") else None,
            ends_at=datetime.fromisoformat(data["ends_at"]) if data.get("ends_at") else None,
        )
