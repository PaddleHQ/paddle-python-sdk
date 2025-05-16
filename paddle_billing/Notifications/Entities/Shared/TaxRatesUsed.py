from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Notifications.Entities.Shared.Totals import Totals


@dataclass
class TaxRatesUsed:
    tax_rate: str
    totals: Totals

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TaxRatesUsed:
        return TaxRatesUsed(
            tax_rate=data["tax_rate"],
            totals=Totals.from_dict(data["totals"]),
        )
