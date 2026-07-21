from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.CheckoutDomains import CheckoutDomainStatus

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import Pager


class ListCheckoutDomains(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        domain: str | None = None,
        statuses: list[CheckoutDomainStatus] | None = None,
    ):
        self.pager = pager
        self.domain = domain
        self.statuses = statuses if statuses is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ("statuses", self.statuses, CheckoutDomainStatus),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types(
                    field_name, field_type.__name__, invalid_items
                )

    def get_parameters(self) -> dict[str, str]:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.domain:
            parameters["domain"] = self.domain
        if self.statuses:
            parameters["status"] = ",".join(map(enum_stringify, self.statuses))

        return parameters
