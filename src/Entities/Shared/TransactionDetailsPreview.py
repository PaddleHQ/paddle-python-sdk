from __future__                  import annotations
from .TaxRatesUsed               import TaxRatesUsed
from .TransactionTotals          import TransactionTotals
from .TransactionLineItemPreview import TransactionLineItemPreview
from dataclasses                 import dataclass
from typing                      import List


@dataclass
class TransactionDetailsPreview:
    tax_rates_used: List[TaxRatesUsed]
    totals:         TransactionTotals
    line_items:     List[TransactionLineItemPreview]


    @staticmethod
    def from_dict(data: dict) -> TransactionDetailsPreview:
        return TransactionDetailsPreview(
            tax_rates_used = [TaxRatesUsed.from_dict(rate) for rate in data['tax_rates_used']],
            totals         = TransactionTotals.from_dict(data['totals']),
            line_items     = [TransactionLineItemPreview.from_dict(item) for item in data['line_items']],
        )
