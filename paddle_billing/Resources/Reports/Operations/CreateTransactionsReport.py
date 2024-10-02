from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import TransactionsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    CollectionModeFilter,
    CurrencyCodeFilter,
    TransactionOriginFilter,
    TransactionStatusFilter,
    UpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)


@dataclass
class CreateTransactionsReport(CreateReport):
    type: TransactionsReportType
    filters: list[
        CollectionModeFilter | CurrencyCodeFilter | TransactionOriginFilter | TransactionStatusFilter | UpdatedAtFilter
    ] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple:
        return (
            CollectionModeFilter,
            CurrencyCodeFilter,
            TransactionOriginFilter,
            TransactionStatusFilter,
            UpdatedAtFilter,
        )
