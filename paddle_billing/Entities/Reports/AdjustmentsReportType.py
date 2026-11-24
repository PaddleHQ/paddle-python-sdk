from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)

from paddle_billing.Entities.Reports.ReportType import ReportType as ReportType


class AdjustmentsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Adjustments: "AdjustmentsReportType" = member(ReportType.Adjustments.value)
    AdjustmentLineItems: "AdjustmentsReportType" = member(ReportType.AdjustmentLineItems.value)
