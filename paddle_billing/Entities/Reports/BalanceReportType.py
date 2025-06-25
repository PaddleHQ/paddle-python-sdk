from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType


class BalanceReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Balance: "BalanceReportType" = ReportType.Balance.value
