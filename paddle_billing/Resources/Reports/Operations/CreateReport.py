from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any

from paddle_billing.Operation import Operation

from paddle_billing.Entities.Reports import ReportType, ReportFilter

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


@dataclass
class CreateReport(Operation, ABC):
    type: ReportType
    filters: list[ReportFilter] = field(default_factory=list)

    def __post_init__(self):
        allowed_types = self.get_allowed_filters()

        # Validation
        if any(not isinstance(filter_item, allowed_types) for filter_item in self.filters):
            invalid_items = [filter_item for filter_item in self.filters if not isinstance(filter_item, allowed_types)]
            allowed_type_names = list(map(lambda allowed_type: allowed_type.__name__, allowed_types))

            raise InvalidArgumentException.array_contains_invalid_types("filters", allowed_type_names, invalid_items)

    def to_json(self) -> dict[str, Any]:
        parameters: dict[str, Any] = {"type": self.type}

        if self.filters is not None and self.filters != []:
            parameters.update({"filters": [filter_ for filter_ in self.filters]})

        return parameters

    @staticmethod
    @abstractmethod
    def get_allowed_filters() -> tuple[Any]:
        pass
