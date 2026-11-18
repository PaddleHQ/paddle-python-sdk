from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member

from paddle_billing.Entities.Reports.ReportType import ReportType


class AdjustmentsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Adjustments: "AdjustmentsReportType" = member(ReportType.Adjustments.value)
    AdjustmentLineItems: "AdjustmentsReportType" = member(ReportType.AdjustmentLineItems.value)
