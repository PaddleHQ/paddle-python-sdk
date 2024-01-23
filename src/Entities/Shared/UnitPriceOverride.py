from __future__  import annotations
from dataclasses import dataclass
from typing      import List

from src.Entities.Shared.CountryCode import CountryCode
from src.Entities.Shared.Money       import Money


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
