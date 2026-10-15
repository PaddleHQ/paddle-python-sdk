from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Shared import CountryCode, CurrencyCode


@dataclass
class CurrencyDefinition(Entity):
    code: CurrencyCode
    name: str
    decimal_places: int
    can_be_balance: bool
    applicable_countries: list[CountryCode]
    minimum_payment_amount: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CurrencyDefinition:
        return CurrencyDefinition(
            code=CurrencyCode(data["code"]),
            name=data["name"],
            decimal_places=data["decimal_places"],
            can_be_balance=data["can_be_balance"],
            applicable_countries=[CountryCode(country) for country in data["applicable_countries"]],
            minimum_payment_amount=data["minimum_payment_amount"],
        )
