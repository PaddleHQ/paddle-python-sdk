from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.CountryCode import CountryCode
from paddle_billing.Entities.Shared.Money       import Money


@dataclass
class UnitPriceOverride:
    country_codes: list[CountryCode]
    unit_price:    Money


    @staticmethod
    def from_dict(data: dict) -> UnitPriceOverride:
        return UnitPriceOverride(
            country_codes = [CountryCode(code) for code in data['country_codes']],
            unit_price    = Money.from_dict(data['unit_price'])
        )
