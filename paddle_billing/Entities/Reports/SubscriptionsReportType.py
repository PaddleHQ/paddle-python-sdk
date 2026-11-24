from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)

from paddle_billing.Entities.Reports.ReportType import ReportType as ReportType


class SubscriptionsReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Subscriptions: "SubscriptionsReportType" = member(ReportType.Subscriptions.value)
