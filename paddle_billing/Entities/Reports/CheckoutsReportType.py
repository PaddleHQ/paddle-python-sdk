from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member

from paddle_billing.Entities.Reports.ReportType import ReportType


class CheckoutsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Checkouts: "CheckoutsReportType" = member(ReportType.Checkouts.value)
