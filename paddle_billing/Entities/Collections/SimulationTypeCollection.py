from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.SimulationType import SimulationType


class SimulationTypeCollection(Collection[SimulationType]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> SimulationTypeCollection:
        items: list[SimulationType] = [SimulationType.from_dict(item) for item in items_data]

        return SimulationTypeCollection(items, paginator)
