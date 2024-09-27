from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType

class AdjustmentsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Adjustments: "AdjustmentsReportType"         = ReportType.Adjustments
    AdjustmentLineItems: "AdjustmentsReportType" = ReportType.AdjustmentLineItems
