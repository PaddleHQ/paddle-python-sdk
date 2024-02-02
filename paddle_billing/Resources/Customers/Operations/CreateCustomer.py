from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import CustomData


@dataclass
class CreateCustomer:
    email:       str
    name:        str        | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    locale:      str               | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
