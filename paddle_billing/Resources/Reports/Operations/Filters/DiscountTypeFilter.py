from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.EnumStringify import enum_stringify

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter

from paddle_billing.Entities.Discounts.DiscountType import DiscountType

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class DiscountTypeFilter(Filter):
    types: list[DiscountType]

    @staticmethod
    def get_name() -> str:
        return ReportFilterName.Type

    def get_value(self) -> list[str]:
        return list(map(enum_stringify, self.types))
