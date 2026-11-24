from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Settings import BalanceCurrencyCode as BalanceCurrencyCode


@dataclass
class UpdateBalanceCurrency(Operation):
    preferred: BalanceCurrencyCode | Undefined = Undefined()
