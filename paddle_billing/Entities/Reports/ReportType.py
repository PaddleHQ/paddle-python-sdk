from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class ReportType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Adjustments          = 'adjustments'
    AdjustmentLineItems  = 'adjustment_line_items'
    Discounts            = 'discounts'
    ProductsPrices       = 'products_prices'
    Transactions         = 'transactions'
    TransactionLineItems = 'transaction_line_items'
