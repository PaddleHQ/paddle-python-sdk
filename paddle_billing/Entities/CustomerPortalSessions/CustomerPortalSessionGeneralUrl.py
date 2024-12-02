from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CustomerPortalSessionGeneralUrl:
    overview: str

    @staticmethod
    def from_dict(data: dict) -> CustomerPortalSessionGeneralUrl:
        return CustomerPortalSessionGeneralUrl(
            overview=data["overview"],
        )
