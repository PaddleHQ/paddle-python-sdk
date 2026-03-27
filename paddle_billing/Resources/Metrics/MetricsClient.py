from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Metrics.MetricsActiveSubscribers import MetricsActiveSubscribers
from paddle_billing.Entities.Metrics.MetricsChargebacks import MetricsChargebacks
from paddle_billing.Entities.Metrics.MetricsCheckoutConversion import MetricsCheckoutConversion
from paddle_billing.Entities.Metrics.MetricsMonthlyRecurringRevenue import MetricsMonthlyRecurringRevenue
from paddle_billing.Entities.Metrics.MetricsMonthlyRecurringRevenueChange import MetricsMonthlyRecurringRevenueChange
from paddle_billing.Entities.Metrics.MetricsRefunds import MetricsRefunds
from paddle_billing.Entities.Metrics.MetricsRevenue import MetricsRevenue

from paddle_billing.Resources.Metrics.Operations import GetMetrics

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class MetricsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def get_monthly_recurring_revenue(self, operation: GetMetrics) -> MetricsMonthlyRecurringRevenue:
        self.response = self.client.get_raw("/metrics/monthly-recurring-revenue", operation.get_parameters())
        parser = ResponseParser(self.response)

        return MetricsMonthlyRecurringRevenue.from_dict(parser.get_dict())

    def get_monthly_recurring_revenue_change(self, operation: GetMetrics) -> MetricsMonthlyRecurringRevenueChange:
        self.response = self.client.get_raw("/metrics/monthly-recurring-revenue-change", operation.get_parameters())
        parser = ResponseParser(self.response)

        return MetricsMonthlyRecurringRevenueChange.from_dict(parser.get_dict())

    def get_active_subscribers(self, operation: GetMetrics) -> MetricsActiveSubscribers:
        self.response = self.client.get_raw("/metrics/active-subscribers", operation.get_parameters())
        parser = ResponseParser(self.response)

        return MetricsActiveSubscribers.from_dict(parser.get_dict())

    def get_revenue(self, operation: GetMetrics) -> MetricsRevenue:
        self.response = self.client.get_raw("/metrics/revenue", operation.get_parameters())
        parser = ResponseParser(self.response)

        return MetricsRevenue.from_dict(parser.get_dict())

    def get_refunds(self, operation: GetMetrics) -> MetricsRefunds:
        self.response = self.client.get_raw("/metrics/refunds", operation.get_parameters())
        parser = ResponseParser(self.response)

        return MetricsRefunds.from_dict(parser.get_dict())

    def get_chargebacks(self, operation: GetMetrics) -> MetricsChargebacks:
        self.response = self.client.get_raw("/metrics/chargebacks", operation.get_parameters())
        parser = ResponseParser(self.response)

        return MetricsChargebacks.from_dict(parser.get_dict())

    def get_checkout_conversion(self, operation: GetMetrics) -> MetricsCheckoutConversion:
        self.response = self.client.get_raw("/metrics/checkout-conversion", operation.get_parameters())
        parser = ResponseParser(self.response)

        return MetricsCheckoutConversion.from_dict(parser.get_dict())
