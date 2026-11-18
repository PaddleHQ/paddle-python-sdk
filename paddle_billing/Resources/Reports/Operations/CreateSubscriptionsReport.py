from dataclasses import dataclass, field
from typing import Type

from paddle_billing.Entities.Reports import SubscriptionsReportType

from paddle_billing.Resources.Reports.Operations.Filters import (
    CustomerCountryCodeFilter,
    SubscriptionCreatedAtFilter,
    SubscriptionScheduledChangeActionFilter,
    SubscriptionStatusFilter,
)

from paddle_billing.Resources.Reports.Operations.CreateReport import CreateReport
from paddle_billing.Resources.Reports.Operations.Filters.Filter import Filter


@dataclass
class CreateSubscriptionsReport(
    CreateReport[
        SubscriptionsReportType,
        CustomerCountryCodeFilter
        | SubscriptionCreatedAtFilter
        | SubscriptionScheduledChangeActionFilter
        | SubscriptionStatusFilter,
    ]
):
    type: SubscriptionsReportType
    filters: list[
        CustomerCountryCodeFilter
        | SubscriptionCreatedAtFilter
        | SubscriptionScheduledChangeActionFilter
        | SubscriptionStatusFilter
    ] = field(default_factory=list)

    @staticmethod
    def get_allowed_filters() -> tuple[Type[Filter], ...]:
        return (
            CustomerCountryCodeFilter,
            SubscriptionCreatedAtFilter,
            SubscriptionScheduledChangeActionFilter,
            SubscriptionStatusFilter,
        )
