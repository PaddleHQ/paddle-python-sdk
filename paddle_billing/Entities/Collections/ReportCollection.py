from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Report import Report


class ReportCollection(Collection[Report]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> ReportCollection:
        items: list[Report] = [Report.from_dict(item) for item in items_data]

        return ReportCollection(items, paginator)
