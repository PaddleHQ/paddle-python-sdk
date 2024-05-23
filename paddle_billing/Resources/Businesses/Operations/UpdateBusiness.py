from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import Contacts, CustomData, Status


@dataclass
class UpdateBusiness:
    name:           str                   | Undefined = Undefined()
    company_number: str            | None | Undefined = Undefined()
    tax_identifier: str            | None | Undefined = Undefined()
    contacts:       list[Contacts]        | Undefined = Undefined()
    custom_data:    CustomData     | None | Undefined = Undefined()
    status:         Status                | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
