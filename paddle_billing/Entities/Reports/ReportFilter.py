from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Reports.ReportFilterName import ReportFilterName as ReportFilterName
from paddle_billing.Entities.Reports.ReportFilterOperator import ReportFilterOperator as ReportFilterOperator


@dataclass
class ReportFilter:
    name: ReportFilterName
    operator: ReportFilterOperator | None
    value: list[Any] | str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ReportFilter:
        return ReportFilter(**data)
