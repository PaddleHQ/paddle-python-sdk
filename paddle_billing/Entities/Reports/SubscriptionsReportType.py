from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType


class SubscriptionsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Subscriptions: "SubscriptionsReportType" = ReportType.Subscriptions.value
