from __future__  import annotations
from dataclasses import dataclass


@dataclass
class AdjustmentCustomerBalance:
    available: str
    reserved:  str
    used:      str


    @staticmethod
    def from_dict(data: dict) -> AdjustmentCustomerBalance:
        return AdjustmentCustomerBalance(
            available = data['available'],
            reserved  = data['reserved'],
            used      = data['used'],
        )
