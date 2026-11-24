from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Shared import Contacts as Contacts, CustomData as CustomData


@dataclass
class CreateBusiness(Operation):
    name: str
    company_number: str | None | Undefined = Undefined()
    tax_identifier: str | None | Undefined = Undefined()
    contacts: list[Contacts] | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
