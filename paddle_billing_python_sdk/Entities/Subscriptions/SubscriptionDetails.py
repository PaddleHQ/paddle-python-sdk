from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.TaxRatesUsed                    import TaxRatesUsed
from paddle_billing_python_sdk.Entities.Shared.TransactionPayoutTotals         import TransactionPayoutTotals
from paddle_billing_python_sdk.Entities.Shared.TransactionPayoutTotalsAdjusted import TransactionPayoutTotalsAdjusted
from paddle_billing_python_sdk.Entities.Shared.TransactionTotals               import TransactionTotals
from paddle_billing_python_sdk.Entities.Shared.TransactionTotalsAdjusted       import TransactionTotalsAdjusted

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionTransactionLineItem import SubscriptionTransactionLineItem


@dataclass
class SubscriptionDetails:
    tax_rates_used:         list[TaxRatesUsed]
    totals:                 TransactionTotals
    adjusted_totals:        TransactionTotalsAdjusted
    payout_totals:          TransactionPayoutTotals
    adjusted_payout_totals: TransactionPayoutTotalsAdjusted
    line_items:             list[SubscriptionTransactionLineItem]


    @staticmethod
    def from_dict(data: dict) -> SubscriptionDetails:
        return SubscriptionDetails(
            totals                 = TransactionTotals.from_dict(data['totals']),
            adjusted_totals        = TransactionTotalsAdjusted.from_dict(data['adjusted_totals']),
            payout_totals          = TransactionPayoutTotals.from_dict(data['payout_totals']),
            adjusted_payout_totals = TransactionPayoutTotalsAdjusted.from_dict(data['adjusted_payout_totals']),
            tax_rates_used         = [TaxRatesUsed.from_dict(tax_rate)                for tax_rate in data.get('tax_rates_used', [])],
            line_items             = [SubscriptionTransactionLineItem.from_dict(item) for item     in data.get('line_items',     [])],
        )
