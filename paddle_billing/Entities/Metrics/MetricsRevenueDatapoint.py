from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class MetricsRevenueDatapoint:
    timestamp: str
    amount: str
    count: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsRevenueDatapoint:
        return MetricsRevenueDatapoint(
            timestamp=data["timestamp"],
            amount=data["amount"],
            count=data["count"],
        )
