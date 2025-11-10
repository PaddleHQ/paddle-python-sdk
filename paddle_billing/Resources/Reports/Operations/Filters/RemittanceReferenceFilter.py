from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class RemittanceReferenceFilter(Filter):
    remittance_references: list[str]

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.RemittanceReference

    def get_value(self) -> list[str]:
        return self.remittance_references
