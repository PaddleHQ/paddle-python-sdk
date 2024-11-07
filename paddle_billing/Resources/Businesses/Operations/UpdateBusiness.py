from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import Contacts, CustomData, Status


@dataclass
class UpdateBusiness(Operation):
    name: str | Undefined = Undefined()
    company_number: str | None | Undefined = Undefined()
    tax_identifier: str | None | Undefined = Undefined()
    contacts: list[Contacts] | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    status: Status | Undefined = Undefined()
