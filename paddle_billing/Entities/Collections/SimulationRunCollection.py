from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.SimulationRun import SimulationRun


class SimulationRunCollection(Collection[SimulationRun]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> SimulationRunCollection:
        items: list[SimulationRun] = [SimulationRun.from_dict(item) for item in items_data]

        return SimulationRunCollection(items, paginator)
