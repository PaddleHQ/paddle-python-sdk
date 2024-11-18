from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Simulation import Simulation


class SimulationCollection(Collection[Simulation]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> SimulationCollection:
        items: list[Simulation] = [Simulation.from_dict(item) for item in items_data]

        return SimulationCollection(items, paginator)
