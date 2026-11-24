from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import ProductsPricesReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    PriceStatusFilter,
    PriceTypeFilter,
    PriceUpdatedAtFilter,
    ProductStatusFilter,
    ProductTypeFilter,
    ProductUpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter


@dataclass
class CreateProductsAndPricesReport(
    CreateReport[
        ProductsPricesReportType,
        PriceStatusFilter
        | PriceTypeFilter
        | PriceUpdatedAtFilter
        | ProductStatusFilter
        | ProductTypeFilter
        | ProductUpdatedAtFilter,
    ]
):
    type: ProductsPricesReportType
    filters: list[
        PriceStatusFilter
        | PriceTypeFilter
        | PriceUpdatedAtFilter
        | ProductStatusFilter
        | ProductTypeFilter
        | ProductUpdatedAtFilter
    ] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (
            PriceStatusFilter,
            PriceTypeFilter,
            PriceUpdatedAtFilter,
            ProductStatusFilter,
            ProductTypeFilter,
            ProductUpdatedAtFilter,
        )
