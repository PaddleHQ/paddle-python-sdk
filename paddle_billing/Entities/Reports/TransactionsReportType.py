from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)

from paddle_billing.Entities.Reports.ReportType import ReportType as ReportType


class TransactionsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Transactions: "TransactionsReportType" = member(ReportType.Transactions.value)
    TransactionLineItems: "TransactionsReportType" = member(ReportType.TransactionLineItems.value)
