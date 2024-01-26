from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Shared.CountryCode import CountryCode
from paddle_billing_python_sdk.Entities.Shared.CustomData  import CustomData
from paddle_billing_python_sdk.Entities.Shared.Status      import Status


@dataclass
class UpdateAddress:
    country_code: CountryCode       | Undefined = Undefined()
    description:  str        | None | Undefined = Undefined()
    first_line:   str        | None | Undefined = Undefined()
    second_line:  str        | None | Undefined = Undefined()
    city:         str        | None | Undefined = Undefined()
    postal_code:  str        | None | Undefined = Undefined()
    region:       str        | None | Undefined = Undefined()
    custom_data:  CustomData | None | Undefined = Undefined()
    status:       Status     | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
