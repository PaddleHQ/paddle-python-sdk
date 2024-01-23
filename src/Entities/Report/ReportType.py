from enum import Enum


class ReportType(Enum):
    Adjustments           = 'adjustments'
    AdjustmentLineItems   = 'adjustment_line_items'
    Transactions          = 'transactions'
    TransactionLineItems  = 'transaction_line_items'
