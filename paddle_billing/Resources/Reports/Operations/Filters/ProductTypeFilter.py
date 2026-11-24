from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.EnumStringify import enum_stringify as enum_stringify

from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter

from paddle_billing.Entities.Shared.CatalogType import CatalogType as CatalogType

from paddle_billing.Entities.Reports import ReportFilterName as ReportFilterName


@dataclass
class ProductTypeFilter(Filter):
    types: list[CatalogType]

    @staticmethod
    def get_name() -> ReportFilterName:
        return ReportFilterName.ProductType

    def get_value(self) -> list[str]:
        return list(map(enum_stringify, self.types))
