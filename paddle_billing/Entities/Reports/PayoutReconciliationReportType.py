from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member

from paddle_billing.Entities.Reports.ReportType import ReportType


class PayoutReconciliationReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PayoutReconciliation: "PayoutReconciliationReportType" = member(ReportType.PayoutReconciliation.value)
