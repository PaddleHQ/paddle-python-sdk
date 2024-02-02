from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import CountryCode, CustomData


@dataclass
class CreateAddress:
    country_code: CountryCode
    description:  str        | None = Undefined()
    first_line:   str        | None = Undefined()
    second_line:  str        | None = Undefined()
    city:         str        | None = Undefined()
    postal_code:  str        | None = Undefined()
    region:       str        | None = Undefined()
    custom_data:  CustomData | None = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
