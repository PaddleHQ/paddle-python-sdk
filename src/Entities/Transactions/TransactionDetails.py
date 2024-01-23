from __future__                                          import annotations
from .TransactionLineItem                                import TransactionLineItem
from dataclasses                                         import dataclass
from src.Entities.Shared.TaxRatesUsed                    import TaxRatesUsed
from src.Entities.Shared.TransactionTotals               import TransactionTotals
from src.Entities.Shared.TransactionTotalsAdjusted       import TransactionTotalsAdjusted
from src.Entities.Shared.TransactionPayoutTotals         import TransactionPayoutTotals
from src.Entities.Shared.TransactionPayoutTotalsAdjusted import TransactionPayoutTotalsAdjusted
from typing                                              import List, Optional


@dataclass
class TransactionDetails:
    taxRatesUsed:         List[TaxRatesUsed]
    totals:               TransactionTotals
    adjustedTotals:       Optional[TransactionTotalsAdjusted]
    payoutTotals:         Optional[TransactionPayoutTotals]
    adjustedPayoutTotals: Optional[TransactionPayoutTotalsAdjusted]
    lineItems:            List[TransactionLineItem]


    @classmethod
    def from_dict(cls, data: dict) -> TransactionDetails:
        return TransactionDetails(
            taxRatesUsed         = [TaxRatesUsed.from_dict(tax_rate_used) for tax_rate_used in data['tax_rates_used']],
            totals               = TransactionTotals.from_dict(data['totals']),
            adjustedTotals       = TransactionTotalsAdjusted.from_dict(data['adjusted_totals']) if 'adjusted_totals' in data else None,
            payoutTotals         = TransactionPayoutTotals.from_dict(data['payout_totals']) if 'payout_totals' in data else None,
            adjustedPayoutTotals = TransactionPayoutTotalsAdjusted.from_dict(data['adjusted_payout_totals']) if 'adjusted_payout_totals' in data else None,
            lineItems            = [TransactionLineItem.from_dict(line_item) for line_item in data['line_items']],
        )
