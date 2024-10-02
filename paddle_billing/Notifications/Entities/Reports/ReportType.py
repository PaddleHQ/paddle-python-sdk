from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Adjustments: "ReportType" = "adjustments"
    AdjustmentLineItems: "ReportType" = "adjustment_line_items"
    Discounts: "ReportType" = "discounts"
    ProductsPrices: "ReportType" = "products_prices"
    Transactions: "ReportType" = "transactions"
    TransactionLineItems: "ReportType" = "transaction_line_items"
