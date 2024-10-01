from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.EnumStringify import enum_stringify

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter

from paddle_billing.Entities.Shared.CollectionMode import CollectionMode

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class CollectionModeFilter(Filter):
    collection_modes: list[CollectionMode]

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.CollectionMode

    def get_value(self) -> list[str]:
        return list(map(enum_stringify, self.collection_modes))
