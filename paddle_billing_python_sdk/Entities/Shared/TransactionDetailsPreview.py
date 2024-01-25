from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.TaxRatesUsed               import TaxRatesUsed
from paddle_billing_python_sdk.Entities.Shared.TransactionLineItemPreview import TransactionLineItemPreview
from paddle_billing_python_sdk.Entities.Shared.TransactionTotals          import TransactionTotals


@dataclass
class TransactionDetailsPreview:
    tax_rates_used: list[TaxRatesUsed]
    totals:         TransactionTotals
    line_items:     list[TransactionLineItemPreview]


    @staticmethod
    def from_dict(data: dict) -> TransactionDetailsPreview:
        return TransactionDetailsPreview(
            tax_rates_used = [TaxRatesUsed.from_dict(rate) for rate in data['tax_rates_used']],
            totals         = TransactionTotals.from_dict(data['totals']),
            line_items     = [TransactionLineItemPreview.from_dict(item) for item in data['line_items']],
        )
