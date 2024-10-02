from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import DiscountsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    DiscountStatusFilter,
    DiscountTypeFilter,
    UpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)


@dataclass
class CreateDiscountsReport(CreateReport):
    type: DiscountsReportType
    filters: list[DiscountStatusFilter | DiscountTypeFilter | UpdatedAtFilter] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple:
        return (
            DiscountStatusFilter,
            DiscountTypeFilter,
            UpdatedAtFilter,
        )
