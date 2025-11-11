from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import PayoutReconciliationReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    RemittanceReferenceFilter,
    TransactionUpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)


@dataclass
class CreatePayoutReconciliationReport(CreateReport):
    type: PayoutReconciliationReportType
    filters: list[RemittanceReferenceFilter | TransactionUpdatedAtFilter] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[RemittanceReferenceFilter | TransactionUpdatedAtFilter]:
        return (
            RemittanceReferenceFilter,
            TransactionUpdatedAtFilter,
        )
