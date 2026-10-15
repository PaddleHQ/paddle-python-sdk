from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Countries import CountryDefinitionTaxMode
from paddle_billing.Entities.Shared import CountryCode, CountryCodeIso3, CurrencyCode, CurrencyCodePayouts


@dataclass
class CountryDefinition(Entity):
    iso: CountryCode
    iso3: CountryCodeIso3
    name: str
    printable_name: str
    uses_postal_code: bool
    transaction_currency: CurrencyCode
    payout_currency: CurrencyCodePayouts
    allow_sales: bool
    has_regions: bool
    tax_mode: CountryDefinitionTaxMode

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CountryDefinition:
        return CountryDefinition(
            iso=CountryCode(data["iso"]),
            iso3=CountryCodeIso3(data["iso3"]),
            name=data["name"],
            printable_name=data["printable_name"],
            uses_postal_code=data["uses_postal_code"],
            transaction_currency=CurrencyCode(data["transaction_currency"]),
            payout_currency=CurrencyCodePayouts(data["payout_currency"]),
            allow_sales=data["allow_sales"],
            has_regions=data["has_regions"],
            tax_mode=CountryDefinitionTaxMode(data["tax_mode"]),
        )
