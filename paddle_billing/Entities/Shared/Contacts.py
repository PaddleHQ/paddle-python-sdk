from __future__  import annotations
from dataclasses import dataclass


@dataclass
class Contacts:
    name:  str
    email: str


    @staticmethod
    def from_dict(data: dict) -> Contacts:
        return Contacts(
            name  = data['name'],
            email = data['email'],
        )
