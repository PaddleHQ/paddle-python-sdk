from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member

from paddle_billing.Entities.Reports.ReportType import ReportType


class BalanceReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Balance: "BalanceReportType" = member(ReportType.Balance.value)
