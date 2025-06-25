from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class CustomerPortalSessionGeneralUrl:
    overview: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> CustomerPortalSessionGeneralUrl:
        return CustomerPortalSessionGeneralUrl(
            overview=data["overview"],
        )
