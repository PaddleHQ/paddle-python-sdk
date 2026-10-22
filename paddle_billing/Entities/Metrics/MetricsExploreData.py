from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Metrics.MetricEntity import MetricEntity
from paddle_billing.Entities.Metrics.MetricsBucketInterval import MetricsBucketInterval
from paddle_billing.Entities.Metrics.MetricsExploreFields import MetricsExploreFields
from paddle_billing.Entities.Metrics.MetricsExploreSeries import MetricsExploreSeries
from paddle_billing.Entities.Shared import CurrencyCode


@dataclass
class MetricsExploreData(Entity):
    entity: MetricEntity
    interval: MetricsBucketInterval
    starts_at: datetime
    ends_at: datetime
    updated_at: datetime
    fields: MetricsExploreFields
    series: list[MetricsExploreSeries]
    currency_code: CurrencyCode | None = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsExploreData:
        return MetricsExploreData(
            entity=MetricEntity(data["entity"]),
            interval=MetricsBucketInterval(data["interval"]),
            starts_at=datetime.fromisoformat(data["starts_at"]),
            ends_at=datetime.fromisoformat(data["ends_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            fields=MetricsExploreFields.from_dict(data["fields"]),
            series=[MetricsExploreSeries.from_dict(series) for series in data["series"]],
            currency_code=CurrencyCode(data["currency_code"]) if data.get("currency_code") else None,
        )
