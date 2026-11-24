from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any, Generic, Type, TypeVar

from paddle_billing.Operation import Operation as Operation

# Unused here since CreateReport became generic; kept so existing imports from this module still work.
from paddle_billing.Entities.Reports import ReportType as ReportType, ReportFilter as ReportFilter  # noqa: F401
from paddle_billing.PaddleStrEnum import PaddleStrEnum as PaddleStrEnum
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import (
    InvalidArgumentException as InvalidArgumentException,
)

ReportTypeT = TypeVar("ReportTypeT", bound=PaddleStrEnum)
FilterT = TypeVar("FilterT", bound=Filter)


@dataclass
class CreateReport(Operation, ABC, Generic[ReportTypeT, FilterT]):
    type: ReportTypeT
    filters: list[FilterT] = field(default_factory=list)

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
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        pass
