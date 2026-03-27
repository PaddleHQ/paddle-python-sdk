from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class MetricsCountDatapoint:
    timestamp: str
    count: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsCountDatapoint:
        return MetricsCountDatapoint(
            timestamp=data["timestamp"],
            count=data["count"],
        )
