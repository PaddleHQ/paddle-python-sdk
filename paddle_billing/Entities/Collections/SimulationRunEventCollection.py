from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.SimulationRunEvent import SimulationRunEvent


class SimulationRunEventCollection(Collection[SimulationRunEvent]):
    @classmethod
    def from_list(
        cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None
    ) -> SimulationRunEventCollection:
        items: list[SimulationRunEvent] = [SimulationRunEvent.from_dict(item) for item in items_data]

        return SimulationRunEventCollection(items, paginator)
