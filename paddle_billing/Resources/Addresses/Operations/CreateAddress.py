from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Shared import CountryCode as CountryCode, CustomData as CustomData


@dataclass
class CreateAddress(Operation):
    country_code: CountryCode
    description: str | None | Undefined = Undefined()
    first_line: str | None | Undefined = Undefined()
    second_line: str | None | Undefined = Undefined()
    city: str | None | Undefined = Undefined()
    postal_code: str | None | Undefined = Undefined()
    region: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
