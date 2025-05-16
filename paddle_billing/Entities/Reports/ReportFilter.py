from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Reports import ReportFilterName, ReportFilterOperator


@dataclass
class ReportFilter:
    name: ReportFilterName
    operator: ReportFilterOperator | None
    value: list[Any] | str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> ReportFilter:
        return ReportFilter(**data)
