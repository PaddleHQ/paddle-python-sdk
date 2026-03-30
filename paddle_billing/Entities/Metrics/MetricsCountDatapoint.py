from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class MetricsCountDatapoint:
    timestamp: datetime
    count: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsCountDatapoint:
        return MetricsCountDatapoint(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            count=data["count"],
        )
