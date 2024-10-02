from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportStatus(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Pending: "ReportStatus" = "pending"
    Ready: "ReportStatus" = "ready"
    Failed: "ReportStatus" = "failed"
    Expired: "ReportStatus" = "expired"
