from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType


class CheckoutsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Checkouts: "CheckoutsReportType" = ReportType.Checkouts.value
