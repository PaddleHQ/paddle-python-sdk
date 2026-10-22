from dataclasses import dataclass, field

from paddle_billing.Entities.Reports import SubscriptionsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    CustomerCountryCodeFilter,
    SubscriptionCreatedAtFilter,
    SubscriptionScheduledChangeActionFilter,
    SubscriptionStatusFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import (
    CreateReport,
)


@dataclass
class CreateSubscriptionsReport(CreateReport):
    type: SubscriptionsReportType
    filters: list[
        CustomerCountryCodeFilter
        | SubscriptionCreatedAtFilter
        | SubscriptionScheduledChangeActionFilter
        | SubscriptionStatusFilter
    ] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> (
        tuple[
            CustomerCountryCodeFilter
            | SubscriptionCreatedAtFilter
            | SubscriptionScheduledChangeActionFilter
            | SubscriptionStatusFilter
        ]
    ):
        return (
            CustomerCountryCodeFilter,
            SubscriptionCreatedAtFilter,
            SubscriptionScheduledChangeActionFilter,
            SubscriptionStatusFilter,
        )
