from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ReportStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "ReportStatus" = member("pending")
    Ready: "ReportStatus" = member("ready")
    Failed: "ReportStatus" = member("failed")
    Expired: "ReportStatus" = member("expired")
