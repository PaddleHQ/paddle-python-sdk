from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Adjustments.AdjustmentTotals import AdjustmentTotals


@dataclass
class AdjustmentTaxRatesUsed:
    tax_rate: str
    totals: AdjustmentTotals

    @staticmethod
    def from_dict(data: dict[str, Any]) -> AdjustmentTaxRatesUsed:
        return AdjustmentTaxRatesUsed(
            tax_rate=data["tax_rate"],
            totals=AdjustmentTotals.from_dict(data["totals"]),
        )
