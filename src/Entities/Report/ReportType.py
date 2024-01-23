from enum import StrEnum


class ReportType(StrEnum):
    Adjustments          = 'adjustments'
    AdjustmentLineItems  = 'adjustment_line_items'
    Transactions         = 'transactions'
    TransactionLineItems = 'transaction_line_items'
