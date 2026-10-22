from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Metrics.MetricsAggregation import MetricsAggregation
from paddle_billing.Entities.Metrics.MetricsFieldType import MetricsFieldType


@dataclass
class MetricsExploreFieldMeasure:
    name: str
    type: MetricsFieldType
    field: str | None = None
    agg: MetricsAggregation | None = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsExploreFieldMeasure:
        return MetricsExploreFieldMeasure(
            name=data["name"],
            type=MetricsFieldType(data["type"]),
            field=data.get("field"),
            agg=MetricsAggregation(data["agg"]) if data.get("agg") else None,
        )
