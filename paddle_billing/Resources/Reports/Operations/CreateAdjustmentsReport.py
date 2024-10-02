from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import AdjustmentsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    AdjustmentActionFilter,
    AdjustmentStatusFilter,
    CurrencyCodeFilter,
    UpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)


@dataclass
class CreateAdjustmentsReport(CreateReport):
    type: AdjustmentsReportType
    filters: list[AdjustmentActionFilter | AdjustmentStatusFilter | CurrencyCodeFilter | UpdatedAtFilter] = field(
        default_factory=list
    )

    @staticmethod
    def get_allowed_filters() -> tuple:
        return (
            AdjustmentActionFilter,
            AdjustmentStatusFilter,
            CurrencyCodeFilter,
            UpdatedAtFilter,
        )
