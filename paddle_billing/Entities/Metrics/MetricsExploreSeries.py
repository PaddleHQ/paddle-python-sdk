from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Metrics.MetricsExploreDataPoint import MetricsExploreDataPoint


@dataclass
class MetricsExploreSeries:
    dimensions: dict[str, str]
    timeseries: list[MetricsExploreDataPoint]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsExploreSeries:
        return MetricsExploreSeries(
            dimensions=dict(data["dimensions"]),
            timeseries=[MetricsExploreDataPoint.from_dict(point) for point in data["timeseries"]],
        )
