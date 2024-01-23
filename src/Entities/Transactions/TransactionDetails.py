from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.TaxRatesUsed                    import TaxRatesUsed
from src.Entities.Shared.TransactionPayoutTotals         import TransactionPayoutTotals
from src.Entities.Shared.TransactionPayoutTotalsAdjusted import TransactionPayoutTotalsAdjusted
from src.Entities.Shared.TransactionTotals               import TransactionTotals
from src.Entities.Shared.TransactionTotalsAdjusted       import TransactionTotalsAdjusted

from src.Entities.Transactions.TransactionLineItem import TransactionLineItem


@dataclass
class TransactionDetails:
    taxRatesUsed:         list[TaxRatesUsed]
    totals:               TransactionTotals
    adjustedTotals:       TransactionTotalsAdjusted | None
    payoutTotals:         TransactionPayoutTotals | None
    adjustedPayoutTotals: TransactionPayoutTotalsAdjusted | None
    lineItems:            list[TransactionLineItem]


    @staticmethod
    def from_dict(data: dict) -> TransactionDetails:
        return TransactionDetails(
            taxRatesUsed         = [TaxRatesUsed.from_dict(tax_rate_used) for tax_rate_used in data['tax_rates_used']],
            totals               = TransactionTotals.from_dict(data['totals']),
            adjustedTotals       = TransactionTotalsAdjusted.from_dict(data['adjusted_totals']) if 'adjusted_totals' in data else None,
            payoutTotals         = TransactionPayoutTotals.from_dict(data['payout_totals']) if 'payout_totals' in data else None,
            adjustedPayoutTotals = TransactionPayoutTotalsAdjusted.from_dict(data['adjusted_payout_totals']) if 'adjusted_payout_totals' in data else None,
            lineItems            = [TransactionLineItem.from_dict(line_item) for line_item in data['line_items']],
        )
