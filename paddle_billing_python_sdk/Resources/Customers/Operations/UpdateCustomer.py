from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Shared.CustomData import CustomData
from paddle_billing_python_sdk.Entities.Shared.Status     import Status


@dataclass
class CreatePrice:
    email:       str | None | Undefined        = Undefined()
    name:        str | None | Undefined        = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    locale:      str | None | Undefined        = Undefined()
    status:      Status | None | Undefined     = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
