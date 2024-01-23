from __future__  import annotations
from dataclasses import dataclass
from typing      import List

from src.Entities.Shared.TaxRatesUsed                    import TaxRatesUsed
from src.Entities.Shared.TransactionPayoutTotals         import TransactionPayoutTotals
from src.Entities.Shared.TransactionPayoutTotalsAdjusted import TransactionPayoutTotalsAdjusted
from src.Entities.Shared.TransactionTotals               import TransactionTotals
from src.Entities.Shared.TransactionTotalsAdjusted       import TransactionTotalsAdjusted

from src.Entities.Subscriptions.SubscriptionTransactionLineItem import SubscriptionTransactionLineItem


@dataclass
class SubscriptionDetails:
    tax_rates_used:         List[TaxRatesUsed]
    totals:                 TransactionTotals
    adjusted_totals:        TransactionTotalsAdjusted
    payout_totals:          TransactionPayoutTotals
    adjusted_payout_totals: TransactionPayoutTotalsAdjusted
    line_items:             List[SubscriptionTransactionLineItem]


    @staticmethod
    def from_dict(data: dict) -> SubscriptionDetails:
        return SubscriptionDetails(
            tax_rates_used         = [TaxRatesUsed.from_dict(tax_rate) for tax_rate in data.get('tax_rates_used', [])],
            totals                 = TransactionTotals.from_dict(data['totals']),
            adjusted_totals        = TransactionTotalsAdjusted.from_dict(data['adjusted_totals']),
            payout_totals          = TransactionPayoutTotals.from_dict(data['payout_totals']),
            adjusted_payout_totals = TransactionPayoutTotalsAdjusted.from_dict(data['adjusted_payout_totals']),
            line_items             = [SubscriptionTransactionLineItem.from_dict(item) for item in data.get('line_items', [])]
        )
