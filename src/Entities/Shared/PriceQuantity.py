from __future__  import annotations
from dataclasses import dataclass


@dataclass
class PriceQuantity:
    minimum: int
    maximum: int


    @staticmethod
    def from_dict(data: dict) -> PriceQuantity:
        return PriceQuantity(
            minimum = data['minimum'],
            maximum = data['maximum'],
        )
