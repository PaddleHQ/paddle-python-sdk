from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Reports import ReportFilterName, ReportFilterOperator


@dataclass
class ReportFilter:
    name: ReportFilterName
    operator: ReportFilterOperator | None
    value: list | str

    @staticmethod
    def from_dict(data: dict) -> ReportFilter:
        return ReportFilter(**data)
