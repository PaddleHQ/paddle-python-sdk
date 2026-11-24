from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)

from paddle_billing.Entities.Reports.ReportType import ReportType as ReportType


class BalanceReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Balance: "BalanceReportType" = member(ReportType.Balance.value)
