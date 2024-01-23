from dataclasses import dataclass


@dataclass
class TransactionCreateItem:
    priceId:  str
    quantity: int
