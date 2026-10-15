from dataclasses import dataclass
from datetime import date, datetime
from typing import Any

from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Metrics import (
    MetricEntity,
    MetricsAggregation,
    MetricsBucketInterval,
    MetricsFilterOperator,
    MetricsSortDirection,
)
from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class ExploreMeasure:
    field: str
    agg: MetricsAggregation | None | Undefined = Undefined()


@dataclass
class ExploreFilter:
    field: str
    op: MetricsFilterOperator
    value: list[str]


@dataclass
class ExploreOrderBy:
    field: str
    dir: MetricsSortDirection


@dataclass
class RunExploreMetricsQuery(Operation):
    entity: MetricEntity
    date_from: DateTime | datetime | date | str
    date_to: DateTime | datetime | date | str
    measures: list[ExploreMeasure]
    interval: MetricsBucketInterval | Undefined = Undefined()
    dimensions: list[str] | Undefined = Undefined()
    filters: list[ExploreFilter] | Undefined = Undefined()
    order_by: list[ExploreOrderBy] | Undefined = Undefined()
    per_page: int | Undefined = Undefined()

    def to_json(self) -> dict[str, Any]:
        payload = {
            "entity": self.entity,
            "from": self._format_boundary(self.date_from),
            "to": self._format_boundary(self.date_to),
            "measures": self.measures,
            "interval": self.interval,
            "dimensions": self.dimensions,
            "filters": self.filters,
            "order_by": self.order_by,
            "per_page": self.per_page,
        }

        return {key: value for key, value in payload.items() if not isinstance(value, Undefined)}

    @staticmethod
    def _format_boundary(value: DateTime | datetime | date | str) -> str:
        if isinstance(value, datetime):
            return str(DateTime.from_datetime(value))

        if isinstance(value, date):
            return value.isoformat()

        return str(value)
