from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Metrics.MetricsAggregation import MetricsAggregation
from paddle_billing.Entities.Metrics.MetricsFieldType import MetricsFieldType


@dataclass
class MetricEntityMeasure:
    name: str
    type: MetricsFieldType
    aggs: list[MetricsAggregation] | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricEntityMeasure:
        aggs = data.get("aggs")

        return MetricEntityMeasure(
            name=data["name"],
            type=MetricsFieldType(data["type"]),
            aggs=[MetricsAggregation(agg) for agg in aggs] if aggs is not None else None,
        )
