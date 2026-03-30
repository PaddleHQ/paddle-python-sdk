from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class MetricsAmountDatapoint:
    timestamp: datetime
    amount: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsAmountDatapoint:
        return MetricsAmountDatapoint(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            amount=data["amount"],
        )
