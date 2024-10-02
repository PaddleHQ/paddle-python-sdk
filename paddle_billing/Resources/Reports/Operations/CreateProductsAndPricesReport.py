from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import ProductsPricesReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    PriceStatusFilter,
    PriceTypeFilter,
    PriceUpdatedAtFilter,
    ProductStatusFilter,
    ProductTypeFilter,
    ProductUpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)


@dataclass
class CreateProductsAndPricesReport(CreateReport):
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
    def get_allowed_filters() -> tuple:
        return (
            PriceStatusFilter,
            PriceTypeFilter,
            PriceUpdatedAtFilter,
            ProductStatusFilter,
            ProductTypeFilter,
            ProductUpdatedAtFilter,
        )
