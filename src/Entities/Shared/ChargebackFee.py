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
        return ChargebackFee(
            amount   = data['amount'],
            original = Original.from_dict(data['original']) if 'original' in data else None,
        )
