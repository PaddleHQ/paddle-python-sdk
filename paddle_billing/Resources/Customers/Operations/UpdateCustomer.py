from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import CustomData, Status


@dataclass
class UpdateCustomer(Operation):
    email: str | Undefined = Undefined()
    name: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    locale: str | Undefined = Undefined()
    status: Status | Undefined = Undefined()
