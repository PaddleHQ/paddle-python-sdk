from paddle_billing.PaddleStrEnum import PaddleStrEnum


class ReportType(PaddleStrEnum):
    Adjustments          = 'adjustments'
    AdjustmentLineItems  = 'adjustment_line_items'
    Transactions         = 'transactions'
    TransactionLineItems = 'transaction_line_items'
