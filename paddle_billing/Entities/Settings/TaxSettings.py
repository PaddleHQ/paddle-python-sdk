from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Settings.DefaultTaxMode import DefaultTaxMode


@dataclass
class TaxSettings(Entity):
    default_tax_mode: DefaultTaxMode

    @staticmethod
    def from_dict(data: dict[str, Any]) -> TaxSettings:
        return TaxSettings(
            default_tax_mode=DefaultTaxMode(data["default_tax_mode"]),
        )
