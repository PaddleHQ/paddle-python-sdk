from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType


class TransactionsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Transactions: "TransactionsReportType" = ReportType.Transactions.value
    TransactionLineItems: "TransactionsReportType" = ReportType.TransactionLineItems.value
