from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.DateTime import DateTime

from paddle_billing.Entities.Reports import ReportFilterOperator

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class UpdatedAtFilter(Filter):
    operator: ReportFilterOperator
    value: DateTime

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.UpdatedAt

    def get_operator(self) -> ReportFilterOperator | None:
        return self.operator

    def get_value(self) -> str:
        return self.value.format()

    @staticmethod
    def gte(value: DateTime) -> UpdatedAtFilter:
        return UpdatedAtFilter(value=value, operator=ReportFilterOperator.Gte)

    @staticmethod
    def lt(value: DateTime) -> UpdatedAtFilter:
        return UpdatedAtFilter(value=value, operator=ReportFilterOperator.Lt)
