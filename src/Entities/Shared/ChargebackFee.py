from __future__  import annotations
from .Original   import Original
from dataclasses import dataclass
from typing      import Optional


@dataclass
class ChargebackFee:
    amount:   str
    original: Optional[Original]


    @staticmethod
    def from_dict(data: dict) -> ChargebackFee:
        original = Original.from_dict(data['original']) if 'original' in data else None

        return ChargebackFee(
            amount   = data['amount'],
            original = original,
        )
