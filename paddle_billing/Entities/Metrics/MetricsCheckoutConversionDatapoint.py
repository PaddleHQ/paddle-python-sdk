from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class MetricsCheckoutConversionDatapoint:
    timestamp: datetime
    count: int
    completed_count: int
    rate: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsCheckoutConversionDatapoint:
        return MetricsCheckoutConversionDatapoint(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            count=data["count"],
            completed_count=data["completed_count"],
            rate=data["rate"],
        )
