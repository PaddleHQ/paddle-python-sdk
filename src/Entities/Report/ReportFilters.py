from __future__         import annotations
from dataclasses        import dataclass
from .ReportName        import ReportName
from .ReportOperator    import ReportOperator
from typing             import Union, Optional


@dataclass
class ReportFilters:
    name:       ReportName
    operator:   Optional[ReportOperator]
    value:      Union[list, str]


    @staticmethod
    def from_dict(data: dict) -> ReportFilters:
        return ReportFilters(**data)
