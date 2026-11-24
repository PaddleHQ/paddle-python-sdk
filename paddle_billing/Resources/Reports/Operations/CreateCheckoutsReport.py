from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import CheckoutsReportType as CheckoutsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    CheckoutCreatedAtFilter as CheckoutCreatedAtFilter,
    CustomerCountryCodeFilter as CustomerCountryCodeFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport as CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter as Filter


@dataclass
class CreateCheckoutsReport(CreateReport[CheckoutsReportType, CheckoutCreatedAtFilter | CustomerCountryCodeFilter]):
    type: CheckoutsReportType
    filters: list[CheckoutCreatedAtFilter | CustomerCountryCodeFilter] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (
            CheckoutCreatedAtFilter,
            CustomerCountryCodeFilter,
        )
