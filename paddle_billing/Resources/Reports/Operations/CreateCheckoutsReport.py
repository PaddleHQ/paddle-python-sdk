from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import CheckoutsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    CheckoutCreatedAtFilter,
    CustomerCountryCodeFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)


@dataclass
class CreateCheckoutsReport(CreateReport):
    type: CheckoutsReportType
    filters: list[CheckoutCreatedAtFilter | CustomerCountryCodeFilter] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[CheckoutCreatedAtFilter | CustomerCountryCodeFilter]:
        return (
            CheckoutCreatedAtFilter,
            CustomerCountryCodeFilter,
        )
