from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member

from paddle_billing.Entities.Reports.ReportType import ReportType


class TransactionsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Transactions: "TransactionsReportType" = member(ReportType.Transactions.value)
    TransactionLineItems: "TransactionsReportType" = member(ReportType.TransactionLineItems.value)
