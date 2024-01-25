from __future__  import annotations
from dataclasses import dataclass


@dataclass
class BusinessesContacts:
    name:  str
    email: str


    @staticmethod
    def from_dict(data: dict) -> BusinessesContacts:
        return BusinessesContacts(
            name  = data['name'],
            email = data['email'],
        )
