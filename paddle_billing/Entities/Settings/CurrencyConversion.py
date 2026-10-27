from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class CurrencyConversion:
    enabled: bool

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CurrencyConversion:
        return CurrencyConversion(
            enabled=data["enabled"],
        )
