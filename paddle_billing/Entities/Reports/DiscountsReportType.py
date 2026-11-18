from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member

from paddle_billing.Entities.Reports.ReportType import ReportType


class DiscountsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Discounts: "DiscountsReportType" = member(ReportType.Discounts.value)
