from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Events.EventTypeName import EventTypeName
from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing.HasParameters import HasParameters
from paddle_billing.Resources.Shared.Operations import Pager


class ListEvents(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        event_types: list[EventTypeName] | None = None,
        filter: str | None = None,
        end: DateTime | None = None,
        start: DateTime | None = None,
    ):
        self.pager = pager
        self.filter = filter
        self.end = end
        self.start = start
        self.event_types = event_types if event_types is not None else []

        for field_name, field_value, field_type in [
            ("event_types", self.event_types, EventTypeName),
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
        if self.event_types:
            parameters["event_type"] = ",".join(map(enum_stringify, self.event_types))
        if self.filter:
            parameters["filter"] = self.filter
        if self.end:
            parameters["to"] = self.end.format()
        if self.start:
            parameters["from"] = self.start.format()

        return parameters
