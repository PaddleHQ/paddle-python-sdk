from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import DiscountsReportType as DiscountsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    DiscountStatusFilter as DiscountStatusFilter,
    DiscountTypeFilter as DiscountTypeFilter,
    UpdatedAtFilter as UpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport as CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter


@dataclass
class CreateDiscountsReport(
    CreateReport[DiscountsReportType, DiscountStatusFilter | DiscountTypeFilter | UpdatedAtFilter]
):
    type: DiscountsReportType
    filters: list[DiscountStatusFilter | DiscountTypeFilter | UpdatedAtFilter] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (
            DiscountStatusFilter,
            DiscountTypeFilter,
            UpdatedAtFilter,
        )
