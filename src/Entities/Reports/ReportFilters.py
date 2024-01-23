from __future__  import annotations
from dataclasses import dataclass
from typing      import Union, Optional

from src.Entities.Reports.ReportName     import ReportName
from src.Entities.Reports.ReportOperator import ReportOperator


@dataclass
class ReportFilters:
    name:     ReportName
    operator: Optional[ReportOperator]
    value:    Union[list, str]


    @staticmethod
    def from_dict(data: dict) -> ReportFilters:
        return ReportFilters(**data)
