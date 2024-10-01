from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.EnumStringify import enum_stringify

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter

from paddle_billing.Entities.Shared.Action import Action

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class AdjustmentActionFilter(Filter):
    actions: list[Action]

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.Action

    def get_value(self) -> list[str]:
        return list(map(enum_stringify, self.actions))
