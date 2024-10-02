from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType


class DiscountsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Discounts: "DiscountsReportType" = ReportType.Discounts.value
