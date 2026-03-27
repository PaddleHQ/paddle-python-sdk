from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class MetricsAmountDatapoint:
    timestamp: str
    amount: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsAmountDatapoint:
        return MetricsAmountDatapoint(
            timestamp=data["timestamp"],
            amount=data["amount"],
        )
