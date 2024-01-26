from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Shared.Contacts   import Contacts
from paddle_billing_python_sdk.Entities.Shared.CustomData import CustomData
from paddle_billing_python_sdk.Entities.Shared.Status     import Status


@dataclass
class UpdateBusiness:
    name:           str | Undefined               = Undefined
    company_number: str | None | Undefined        = Undefined()
    tax_identifier: str | None | Undefined        = Undefined()
    contacts:       list[Contacts] | Undefined    = Undefined()
    custom_data:    CustomData | None | Undefined = Undefined()
    status:         Status | None | Undefined     = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)