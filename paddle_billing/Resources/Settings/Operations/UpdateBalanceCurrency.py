from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Settings import BalanceCurrencyCode


@dataclass
class UpdateBalanceCurrency(Operation):
    preferred: BalanceCurrencyCode | Undefined = Undefined()
