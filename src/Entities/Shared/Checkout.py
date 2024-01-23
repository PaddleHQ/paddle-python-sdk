from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional


@dataclass
class Checkout:
    url: Optional[str]


    @staticmethod
    def from_dict(data: dict) -> Checkout:
        return Checkout(url=data.get('url'))
