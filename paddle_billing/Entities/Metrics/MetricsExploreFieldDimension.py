from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Metrics.MetricsFieldType import MetricsFieldType


@dataclass
class MetricsExploreFieldDimension:
    name: str
    type: MetricsFieldType

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsExploreFieldDimension:
        return MetricsExploreFieldDimension(name=data["name"], type=MetricsFieldType(data["type"]))
