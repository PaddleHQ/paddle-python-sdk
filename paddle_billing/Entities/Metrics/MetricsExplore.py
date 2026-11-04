from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Metrics.MetricEntity import MetricEntity
from paddle_billing.Entities.Metrics.MetricsBucketInterval import MetricsBucketInterval
from paddle_billing.Entities.Metrics.MetricsExploreFields import MetricsExploreFields
from paddle_billing.Entities.Metrics.MetricsExplorePagination import MetricsExplorePagination
from paddle_billing.Entities.Metrics.MetricsExploreSeries import MetricsExploreSeries
from paddle_billing.Entities.Shared import CurrencyCode


@dataclass
class MetricsExplore:
    entity: MetricEntity
    interval: MetricsBucketInterval
    starts_at: datetime
    ends_at: datetime
    updated_at: datetime
    fields: MetricsExploreFields
    series: list[MetricsExploreSeries]
    pagination: MetricsExplorePagination
    currency_code: CurrencyCode | None = None

    @staticmethod
    def from_dict(body: dict[str, Any]) -> MetricsExplore:
        data = body["data"]

        return MetricsExplore(
            entity=MetricEntity(data["entity"]),
            interval=MetricsBucketInterval(data["interval"]),
            starts_at=datetime.fromisoformat(data["starts_at"]),
            ends_at=datetime.fromisoformat(data["ends_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            fields=MetricsExploreFields.from_dict(data["fields"]),
            series=[MetricsExploreSeries.from_dict(series) for series in data["series"]],
            pagination=MetricsExplorePagination.from_dict(body["meta"]["pagination"]),
            currency_code=CurrencyCode(data["currency_code"]) if data.get("currency_code") else None,
        )
