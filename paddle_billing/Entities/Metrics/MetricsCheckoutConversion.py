from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Metrics.MetricsCheckoutConversionDatapoint import MetricsCheckoutConversionDatapoint
from paddle_billing.Entities.Metrics.MetricsInterval import MetricsInterval


@dataclass
class MetricsCheckoutConversion(Entity):
    timeseries: list[MetricsCheckoutConversionDatapoint]
    starts_at: str
    ends_at: str
    interval: MetricsInterval
    updated_at: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsCheckoutConversion:
        return MetricsCheckoutConversion(
            timeseries=[MetricsCheckoutConversionDatapoint.from_dict(dp) for dp in data.get("timeseries", [])],
            starts_at=data["starts_at"],
            ends_at=data["ends_at"],
            interval=MetricsInterval(data["interval"]),
            updated_at=data["updated_at"],
        )
