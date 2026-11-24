from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class ReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Adjustments: "ReportType" = member("adjustments")
    AdjustmentLineItems: "ReportType" = member("adjustment_line_items")
    Discounts: "ReportType" = member("discounts")
    ProductsPrices: "ReportType" = member("products_prices")
    Transactions: "ReportType" = member("transactions")
    TransactionLineItems: "ReportType" = member("transaction_line_items")
    Balance: "ReportType" = member("balance")
    PayoutReconciliation: "ReportType" = member("payout_reconciliation")
    Checkouts: "ReportType" = member("checkouts")
    Subscriptions: "ReportType" = member("subscriptions")
