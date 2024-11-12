from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Paypal:
    email: str
    reference: str

    @staticmethod
    def from_dict(data: dict) -> Paypal:
        return Paypal(
            email=data["email"],
            reference=data["reference"],
        )
