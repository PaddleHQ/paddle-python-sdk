from paddle_billing_python_sdk.EnumStringify import enum_stringify
from paddle_billing_python_sdk.HasParameters import HasParameters

from paddle_billing_python_sdk.Entities.Shared.Status import Status

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager


class ListReports(HasParameters):
    def __init__(
        self,
        pager:    Pager        = None,
        statuses: list[Status] = None,
    ):
        self.pager    = pager
        self.statuses = statuses if statuses is not None else []

        # Validation
        for field_name, field_value, field_type in [('statuses', self.statuses, Status),]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))

        return parameters
