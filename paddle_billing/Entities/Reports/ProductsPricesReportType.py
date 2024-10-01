from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta

from paddle_billing.Entities.Reports.ReportType import ReportType


class ProductsPricesReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ProductsPrices: "ProductsPricesReportType" = ReportType.ProductsPrices.value
