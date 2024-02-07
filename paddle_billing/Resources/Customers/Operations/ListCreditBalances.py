from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import CurrencyCode

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


class ListCreditBalances(HasParameters):
    def __init__(
        self,
        currency_code: list[CurrencyCode] = None,
    ):
        self.currency_code = currency_code if currency_code is not None else []

        # Validation
        for field_name, field_value, field_type in [('currency_code', self.currency_code, CurrencyCode)]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        parameters = {}
        if self.currency_code:
            parameters['currency_code'] = ','.join(map(enum_stringify, self.currency_code))

        return parameters
