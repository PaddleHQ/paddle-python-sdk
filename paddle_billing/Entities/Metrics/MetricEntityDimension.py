from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Metrics.MetricsFieldType import MetricsFieldType as MetricsFieldType
from paddle_billing.Entities.Metrics.MetricsFilterOperator import MetricsFilterOperator as MetricsFilterOperator


@dataclass
class MetricEntityDimension:
    name: str
    type: MetricsFieldType
    filter_ops: list[MetricsFilterOperator]
    multi_valued: bool | None = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricEntityDimension:
        return MetricEntityDimension(
            name=data["name"],
            type=MetricsFieldType(data["type"]),
            filter_ops=[MetricsFilterOperator(op) for op in data["filter_ops"]],
            multi_valued=data.get("multi_valued"),
        )
