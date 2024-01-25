from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class ReportCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> ReportCollection:
        from paddle_billing_python_sdk.Entities.Report import Report

        items = [Report.from_dict(item) for item in items_data]

        return ReportCollection(items, paginator)


    def __next__(self):
        return super().__next__()