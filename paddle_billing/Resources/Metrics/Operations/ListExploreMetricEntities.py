from paddle_billing.Entities.Metrics import MetricEntity
from paddle_billing.HasParameters import HasParameters


class ListExploreMetricEntities(HasParameters):
    def __init__(self, entity: MetricEntity | None = None):
        self.entity = entity

    def get_parameters(self) -> dict[str, str]:
        if self.entity is None:
            return {}

        return {"entity": self.entity.value}
