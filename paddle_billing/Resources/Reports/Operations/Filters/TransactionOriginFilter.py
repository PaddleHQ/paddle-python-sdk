from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.EnumStringify import enum_stringify

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter

from paddle_billing.Entities.Shared.TransactionOrigin import TransactionOrigin

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class TransactionOriginFilter(Filter):
    origins: list[TransactionOrigin]

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.Origin

    def get_value(self) -> list[str]:
        return list(map(enum_stringify, self.origins))
