from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import CheckoutsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    CheckoutCreatedAtFilter,
    CustomerCountryCodeFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter


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
