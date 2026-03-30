from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class MetricsRevenueDatapoint:
    timestamp: datetime
    amount: str
    count: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsRevenueDatapoint:
        return MetricsRevenueDatapoint(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            amount=data["amount"],
            count=data["count"],
        )
