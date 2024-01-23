from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.Original import Original


@dataclass
class ChargebackFee:
    amount:   str
    original: Original | None


    @staticmethod
    def from_dict(data: dict) -> ChargebackFee:
        return ChargebackFee(
            amount   = data['amount'],
            original = Original.from_dict(data['original']) if 'original' in data and data['original'] != '' else None,
        )
