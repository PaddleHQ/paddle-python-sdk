from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class MetricsExploreDataPoint:
    timestamp: str
    measures: dict[str, str]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsExploreDataPoint:
        return MetricsExploreDataPoint(timestamp=data["timestamp"], measures=dict(data["measures"]))
