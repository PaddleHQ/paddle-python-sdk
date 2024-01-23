from __future__  import annotations
from .Totals     import Totals
from dataclasses import dataclass


@dataclass
class TaxRatesUsed:
    tax_rate: str
    totals:   Totals


    @staticmethod
    def from_dict(data: dict) -> TaxRatesUsed:
        return TaxRatesUsed(
            tax_rate = data['tax_rate'],
            totals   = Totals.from_dict(data['totals']),
        )
