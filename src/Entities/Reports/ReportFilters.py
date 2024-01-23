from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Reports.ReportName     import ReportName
from src.Entities.Reports.ReportOperator import ReportOperator


@dataclass
class ReportFilters:
    name:     ReportName
    operator: ReportOperator | None
    value:    list | str


    @staticmethod
    def from_dict(data: dict) -> ReportFilters:
        return ReportFilters(**data)
