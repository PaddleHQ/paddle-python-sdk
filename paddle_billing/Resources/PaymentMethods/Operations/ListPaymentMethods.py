from paddle_billing.HasParameters import HasParameters
from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing.Resources.Shared.Operations import Pager


class ListPaymentMethods(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        address_ids: list[str] = None,
        supports_checkout: bool = None,
    ):
        self.pager = pager
        self.address_ids = address_ids
        self.supports_checkout = supports_checkout

        # Validation
        if address_ids is not None:
            invalid_items = [id for id in address_ids if not isinstance(id, str)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types("ids", str.__name__, invalid_items)

    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.address_ids:
            parameters["address_id"] = ",".join(self.address_ids)
        if self.supports_checkout is not None:
            parameters["supports_checkout"] = "true" if self.supports_checkout else "false"

        return parameters
