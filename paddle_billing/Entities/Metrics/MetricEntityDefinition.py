from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Metrics.MetricEntity import MetricEntity
from paddle_billing.Entities.Metrics.MetricEntityDimension import MetricEntityDimension
from paddle_billing.Entities.Metrics.MetricEntityMeasure import MetricEntityMeasure
from paddle_billing.Entities.Metrics.MetricEntityTimeDimension import MetricEntityTimeDimension


@dataclass
class MetricEntityDefinition(Entity):
    entity: MetricEntity
    time_dimension: MetricEntityTimeDimension
    dimensions: list[MetricEntityDimension]
    measures: list[MetricEntityMeasure]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricEntityDefinition:
        return MetricEntityDefinition(
            entity=MetricEntity(data["entity"]),
            time_dimension=MetricEntityTimeDimension.from_dict(data["time_dimension"]),
            dimensions=[MetricEntityDimension.from_dict(dimension) for dimension in data["dimensions"]],
            measures=[MetricEntityMeasure.from_dict(measure) for measure in data["measures"]],
        )
