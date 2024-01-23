from __future__                                   import annotations
from src.Entities.Transactions.TransactionCardType import TransactionCardType
from dataclasses                                  import dataclass
from typing                                       import Optional


@dataclass
class Card:
    type:            TransactionCardType
    last4:           str
    expiry_month:    int
    expiry_year:     int
    cardholder_name: Optional[str]


    @staticmethod
    def from_dict(data: dict) -> Card:
        return Card(
            type            = TransactionCardType(data['type']),
            last4           = data['last4'],
            expiry_month    = data['expiry_month'],
            expiry_year     = data['expiry_year'],
            cardholder_name = data.get('cardholder_name')
        )
