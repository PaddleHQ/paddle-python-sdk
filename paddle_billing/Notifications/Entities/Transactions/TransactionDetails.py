from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Json import json_format_properties

from paddle_billing.Notifications.Entities.Shared.TaxRatesUsed import TaxRatesUsed
from paddle_billing.Notifications.Entities.Shared.TransactionPayoutTotals import TransactionPayoutTotals
from paddle_billing.Notifications.Entities.Shared.TransactionPayoutTotalsAdjusted import TransactionPayoutTotalsAdjusted
from paddle_billing.Notifications.Entities.Shared.TransactionTotals import TransactionTotals
from paddle_billing.Notifications.Entities.Shared.TransactionTotalsAdjusted import TransactionTotalsAdjusted

from paddle_billing.Notifications.Entities.Transactions.TransactionLineItem import TransactionLineItem


@dataclass
@json_format_properties(["lineItems"])
class TransactionDetails:
    tax_rates_used: list[TaxRatesUsed]
    totals: TransactionTotals
    adjusted_totals: TransactionTotalsAdjusted | None
    payout_totals: TransactionPayoutTotals | None
    adjusted_payout_totals: TransactionPayoutTotalsAdjusted | None
    lineItems: list[TransactionLineItem]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TransactionDetails:
        return TransactionDetails(
            totals=TransactionTotals.from_dict(data["totals"]),
            tax_rates_used=[TaxRatesUsed.from_dict(tax_rate_used) for tax_rate_used in data["tax_rates_used"]],
            lineItems=[TransactionLineItem.from_dict(line_item) for line_item in data["line_items"]],
            adjusted_totals=(
                TransactionTotalsAdjusted.from_dict(data["adjusted_totals"]) if data.get("adjusted_totals") else None
            ),
            payout_totals=(
                TransactionPayoutTotals.from_dict(data["payout_totals"]) if data.get("payout_totals") else None
            ),
            adjusted_payout_totals=(
                TransactionPayoutTotalsAdjusted.from_dict(data["adjusted_payout_totals"])
                if data.get("adjusted_payout_totals")
                else None
            ),
        )
