from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import CustomData, Status


@dataclass
class UpdateCustomer:
    email:       str               | Undefined = Undefined()
    name:        str        | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    locale:      str               | Undefined = Undefined()
    status:      Status            | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
