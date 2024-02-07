from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class ReportCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> ReportCollection:
        from paddle_billing.Entities.Report import Report

        items: list[Report] = [Report.from_dict(item) for item in items_data]

        return ReportCollection(items, paginator)


    def __next__(self):
        return super().__next__()
