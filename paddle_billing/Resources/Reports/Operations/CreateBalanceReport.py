from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import BalanceReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    UpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter


@dataclass
class CreateBalanceReport(CreateReport):
    type: BalanceReportType
    filters: list[UpdatedAtFilter] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Filter]:
        return (UpdatedAtFilter,)
