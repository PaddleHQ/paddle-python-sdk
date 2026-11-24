from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.EnumStringify import enum_stringify as enum_stringify

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter

from paddle_billing.Entities.Reports import BalanceMovementType as BalanceMovementType

from paddle_billing.Entities.Reports import ReportFilterName as ReportFilterName


@dataclass
class BalanceMovementTypeFilter(Filter):
    types: list[BalanceMovementType]

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.BalanceMovementType

    def get_value(self) -> list[str]:
        return list(map(enum_stringify, self.types))
