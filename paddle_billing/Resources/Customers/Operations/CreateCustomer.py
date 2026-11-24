from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Shared import CustomData as CustomData


@dataclass
class CreateCustomer(Operation):
    email: str
    name: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    locale: str | Undefined = Undefined()
