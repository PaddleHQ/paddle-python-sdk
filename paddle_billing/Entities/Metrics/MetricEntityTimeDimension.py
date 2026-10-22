from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Metrics.MetricsBucketInterval import MetricsBucketInterval


@dataclass
class MetricEntityTimeDimension:
    intervals: list[MetricsBucketInterval]
    max_lookback_days: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricEntityTimeDimension:
        return MetricEntityTimeDimension(
            intervals=[MetricsBucketInterval(interval) for interval in data["intervals"]],
            max_lookback_days=data["max_lookback_days"],
        )
