from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import TransactionsReportType as TransactionsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    CollectionModeFilter as CollectionModeFilter,
    CurrencyCodeFilter as CurrencyCodeFilter,
    TransactionOriginFilter as TransactionOriginFilter,
    TransactionStatusFilter as TransactionStatusFilter,
    UpdatedAtFilter as UpdatedAtFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport as CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter


@dataclass
class CreateTransactionsReport(
    CreateReport[
        TransactionsReportType,
        CollectionModeFilter | CurrencyCodeFilter | TransactionOriginFilter | TransactionStatusFilter | UpdatedAtFilter,
    ]
):
    type: TransactionsReportType
    filters: list[
        CollectionModeFilter | CurrencyCodeFilter | TransactionOriginFilter | TransactionStatusFilter | UpdatedAtFilter
    ] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (
            CollectionModeFilter,
            CurrencyCodeFilter,
            TransactionOriginFilter,
            TransactionStatusFilter,
            UpdatedAtFilter,
        )
