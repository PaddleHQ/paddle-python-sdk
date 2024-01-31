from __future__  import annotations
from dataclasses import dataclass


@dataclass
class Checkout:
    url: str | None


    @staticmethod
    def from_dict(data: dict) -> Checkout:
        return Checkout(url=data.get('url'))
