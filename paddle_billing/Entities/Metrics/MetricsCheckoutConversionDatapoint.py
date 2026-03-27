from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class MetricsCheckoutConversionDatapoint:
    timestamp: str
    count: int
    completed_count: int
    rate: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsCheckoutConversionDatapoint:
        return MetricsCheckoutConversionDatapoint(
            timestamp=data["timestamp"],
            count=data["count"],
            completed_count=data["completed_count"],
            rate=data["rate"],
        )
