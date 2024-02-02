from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import CountryCode, CustomData, Status


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
