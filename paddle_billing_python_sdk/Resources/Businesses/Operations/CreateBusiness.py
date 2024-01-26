from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Shared.Contacts   import Contacts
from paddle_billing_python_sdk.Entities.Shared.CustomData import CustomData


@dataclass
class CreateBusiness:
    name:           str
    company_number: str | Undefined            = Undefined()
    tax_identifier: str | Undefined            = Undefined()
    contacts:       list[Contacts] | Undefined = Undefined()
    custom_data:    CustomData | Undefined     = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
