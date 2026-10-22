from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Metrics.MetricsExploreFieldDimension import MetricsExploreFieldDimension
from paddle_billing.Entities.Metrics.MetricsExploreFieldMeasure import MetricsExploreFieldMeasure


@dataclass
class MetricsExploreFields:
    dimensions: list[MetricsExploreFieldDimension]
    measures: list[MetricsExploreFieldMeasure]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsExploreFields:
        return MetricsExploreFields(
            dimensions=[MetricsExploreFieldDimension.from_dict(dimension) for dimension in data["dimensions"]],
            measures=[MetricsExploreFieldMeasure.from_dict(measure) for measure in data["measures"]],
        )
