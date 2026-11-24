from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Settings import DefaultTaxMode as DefaultTaxMode


@dataclass
class UpdateTaxSettings(Operation):
    default_tax_mode: DefaultTaxMode | Undefined = Undefined()
