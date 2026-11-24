from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)

from paddle_billing.Entities.Reports.ReportType import ReportType as ReportType


class PayoutReconciliationReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PayoutReconciliation: "PayoutReconciliationReportType" = member(ReportType.PayoutReconciliation.value)
