from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined


@dataclass
class UpdateStatementDescriptorSettings(Operation):
    name: str | Undefined = Undefined()
