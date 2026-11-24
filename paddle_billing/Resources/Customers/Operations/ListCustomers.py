from typing import Any

from paddle_billing.EnumStringify import enum_stringify as enum_stringify
from paddle_billing.HasParameters import HasParameters as HasParameters

from paddle_billing.Entities.Shared import Status as Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import (
    InvalidArgumentException as InvalidArgumentException,
)

from paddle_billing.Resources.Shared.Operations import Pager as Pager


class ListCustomers(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        ids: list[str] | None = None,
        statuses: list[Status] | None = None,
        search: str | None = None,
        emails: list[str] | None = None,
    ):
        self.pager = pager
        self.search = search
        self.ids = ids if ids is not None else []
        self.statuses = statuses if statuses is not None else []
        self.emails = emails if emails is not None else []

        # Validation
        validations: list[tuple[str, list[Any], type]] = [
            ("ids", self.ids, str),
            ("statuses", self.statuses, Status),
            ("emails", self.emails, str),
        ]
        for field_name, field_value, field_type in validations:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types(
                    field_name, field_type.__name__, invalid_items
                )

    def get_parameters(self) -> dict[str, str]:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters["id"] = ",".join(self.ids)
        if self.statuses:
            parameters["status"] = ",".join(map(enum_stringify, self.statuses))
        if self.search:
            parameters["search"] = self.search
        if self.emails:
            parameters["email"] = ",".join(self.emails)

        return parameters
