from __future__   import annotations
from .CountryCode import CountryCode
from .Money       import Money
from dataclasses  import dataclass
from typing       import List


@dataclass
class UnitPriceOverride:
    countryCodes: List[CountryCode]
    unitPrice:    Money


    @staticmethod
    def from_dict(data: dict) -> UnitPriceOverride:
        return UnitPriceOverride(
            countryCodes = [CountryCode(code) for code in data['country_codes']],
            unitPrice    = Money.from_dict(data['unit_price'])
        )
