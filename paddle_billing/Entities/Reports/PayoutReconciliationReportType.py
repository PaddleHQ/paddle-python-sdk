from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType


class PayoutReconciliationReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PayoutReconciliation: "PayoutReconciliationReportType" = ReportType.PayoutReconciliation.value
