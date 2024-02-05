from __future__  import annotations
from dataclasses import asdict, dataclass

from paddle_billing.Entities.Reports import ReportFilterName, ReportFilterOperator


@dataclass
class ReportFilter:
    name:     ReportFilterName
    operator: ReportFilterOperator | None
    value:    list | str


    @staticmethod
    def from_dict(data: dict) -> ReportFilter:
        return ReportFilter(**data)


    def get_parameters(self) -> dict:
        return asdict(self)
