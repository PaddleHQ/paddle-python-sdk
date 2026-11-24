from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)

from paddle_billing.Entities.Reports.ReportType import ReportType as ReportType


class CheckoutsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Checkouts: "CheckoutsReportType" = member(ReportType.Checkouts.value)
