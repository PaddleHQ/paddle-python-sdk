from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.EnumStringify import enum_stringify

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter

from paddle_billing.Entities.Discounts.DiscountStatus import DiscountStatus

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class DiscountStatusFilter(Filter):
    statuses: list[DiscountStatus]

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.Status

    def get_value(self) -> list[str]:
        return list(map(enum_stringify, self.statuses))
