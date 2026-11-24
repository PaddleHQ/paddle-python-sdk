from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import AdjustmentsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    AdjustmentActionFilter,
    AdjustmentStatusFilter,
    CurrencyCodeFilter,
    UpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter


@dataclass
class CreateAdjustmentsReport(
    CreateReport[
        AdjustmentsReportType, AdjustmentActionFilter | AdjustmentStatusFilter | CurrencyCodeFilter | UpdatedAtFilter
    ]
):
    type: AdjustmentsReportType
    filters: list[AdjustmentActionFilter | AdjustmentStatusFilter | CurrencyCodeFilter | UpdatedAtFilter] = field(
        default_factory=list
    )

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (
            AdjustmentActionFilter,
            AdjustmentStatusFilter,
            CurrencyCodeFilter,
            UpdatedAtFilter,
        )
