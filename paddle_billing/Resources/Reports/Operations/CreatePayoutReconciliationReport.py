from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import PayoutReconciliationReportType as PayoutReconciliationReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    BalanceMovementDateFilter as BalanceMovementDateFilter,
    BalanceMovementTypeFilter as BalanceMovementTypeFilter,
    RemittanceReferenceFilter as RemittanceReferenceFilter,
    TransactionUpdatedAtFilter as TransactionUpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport as CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter


@dataclass
class CreatePayoutReconciliationReport(
    CreateReport[
        PayoutReconciliationReportType,
        BalanceMovementDateFilter | BalanceMovementTypeFilter | RemittanceReferenceFilter | TransactionUpdatedAtFilter,
    ]
):
    type: PayoutReconciliationReportType
    filters: list[
        BalanceMovementDateFilter | BalanceMovementTypeFilter | RemittanceReferenceFilter | TransactionUpdatedAtFilter
    ] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (
            BalanceMovementDateFilter,
            BalanceMovementTypeFilter,
            RemittanceReferenceFilter,
            TransactionUpdatedAtFilter,
        )
