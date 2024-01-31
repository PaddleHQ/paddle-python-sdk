from dataclasses import dataclass, field

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Reports.ReportType    import ReportType
from paddle_billing_python_sdk.Entities.Reports.ReportFilters import ReportFilters

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


@dataclass
class CreateReport:
    type:    ReportType
    filters: list[ReportFilters] = field(default_factory=list)


    def __post_init__(self):
        # Validation
        if any(not isinstance(filter_item, ReportFilters) for filter_item in self.filters):
            invalid_items = [filter_item for filter_item in self.filters if not isinstance(filter_item, ReportFilters)]
            raise InvalidArgumentException('filters', 'ReportFilters', ', '.join(map(str, invalid_items)))


    def get_parameters(self) -> dict:
        parameters = {'type': self.type}

        if self.filters is not None and self.filters != []:
            parameters.update({'filters': [filter.get_parameters() for filter in self.filters]})

        return parameters
