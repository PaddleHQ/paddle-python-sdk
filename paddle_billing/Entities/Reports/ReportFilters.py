from __future__  import annotations
from dataclasses import asdict, dataclass

from paddle_billing.Entities.Reports.ReportName     import ReportName
from paddle_billing.Entities.Reports.ReportOperator import ReportOperator


@dataclass
class ReportFilters:
    name:     ReportName
    operator: ReportOperator | None
    value:    list | str


    @staticmethod
    def from_dict(data: dict) -> ReportFilters:
        return ReportFilters(**data)


    def get_parameters(self) -> dict:
        return asdict(self)
