from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Metrics.MetricsInterval import MetricsInterval
from paddle_billing.Entities.Metrics.MetricsRevenueDatapoint import MetricsRevenueDatapoint
from paddle_billing.Entities.Shared import CurrencyCode


@dataclass
class MetricsRevenue(Entity):
    currency_code: CurrencyCode
    timeseries: list[MetricsRevenueDatapoint]
    starts_at: datetime
    ends_at: datetime
    interval: MetricsInterval
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsRevenue:
        return MetricsRevenue(
            currency_code=CurrencyCode(data["currency_code"]),
            timeseries=[MetricsRevenueDatapoint.from_dict(dp) for dp in data.get("timeseries", [])],
            starts_at=datetime.fromisoformat(data["starts_at"]),
            ends_at=datetime.fromisoformat(data["ends_at"]),
            interval=MetricsInterval(data["interval"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
