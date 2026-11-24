from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import BalanceReportType as BalanceReportType

from paddle_billing.Resources.Reports.Operations.Filters import UpdatedAtFilter as UpdatedAtFilter

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport as CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter


@dataclass
class CreateBalanceReport(CreateReport[BalanceReportType, UpdatedAtFilter]):
    """
    Deprecated: Use CreatePayoutReconciliationReport instead.
    """

    type: BalanceReportType
    filters: list[UpdatedAtFilter] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (UpdatedAtFilter,)
