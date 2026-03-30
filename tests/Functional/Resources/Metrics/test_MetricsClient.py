from json import dumps, loads
from paddle_billing.Json import PayloadEncoder
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Metrics import (
    MetricsActiveSubscribers,
    MetricsChargebacks,
    MetricsCheckoutConversion,
    MetricsMonthlyRecurringRevenue,
    MetricsMonthlyRecurringRevenueChange,
    MetricsRefunds,
    MetricsRevenue,
)

from paddle_billing.Resources.Metrics.Operations import GetMetrics

from tests.Utils.ReadsFixture import ReadsFixtures


class TestMetricsClient:
    @mark.parametrize(
        "method, operation, expected_response_body, expected_url, expected_entity_type",
        [
            (
                "get_monthly_recurring_revenue",
                GetMetrics(date_from="2025-09-01", date_to="2025-09-05"),
                ReadsFixtures.read_raw_json_fixture("response/monthly_recurring_revenue"),
                "/metrics/monthly-recurring-revenue?from=2025-09-01&to=2025-09-05",
                MetricsMonthlyRecurringRevenue,
            ),
            (
                "get_monthly_recurring_revenue_change",
                GetMetrics(date_from="2025-09-01", date_to="2025-09-05"),
                ReadsFixtures.read_raw_json_fixture("response/monthly_recurring_revenue_change"),
                "/metrics/monthly-recurring-revenue-change?from=2025-09-01&to=2025-09-05",
                MetricsMonthlyRecurringRevenueChange,
            ),
            (
                "get_active_subscribers",
                GetMetrics(date_from="2025-09-01", date_to="2025-09-05"),
                ReadsFixtures.read_raw_json_fixture("response/active_subscribers"),
                "/metrics/active-subscribers?from=2025-09-01&to=2025-09-05",
                MetricsActiveSubscribers,
            ),
            (
                "get_revenue",
                GetMetrics(date_from="2025-09-01", date_to="2025-09-05"),
                ReadsFixtures.read_raw_json_fixture("response/revenue"),
                "/metrics/revenue?from=2025-09-01&to=2025-09-05",
                MetricsRevenue,
            ),
            (
                "get_refunds",
                GetMetrics(date_from="2025-09-01", date_to="2025-09-05"),
                ReadsFixtures.read_raw_json_fixture("response/refunds"),
                "/metrics/refunds?from=2025-09-01&to=2025-09-05",
                MetricsRefunds,
            ),
            (
                "get_chargebacks",
                GetMetrics(date_from="2025-09-01", date_to="2025-09-05"),
                ReadsFixtures.read_raw_json_fixture("response/chargebacks"),
                "/metrics/chargebacks?from=2025-09-01&to=2025-09-05",
                MetricsChargebacks,
            ),
            (
                "get_checkout_conversion",
                GetMetrics(date_from="2025-09-01", date_to="2025-09-05"),
                ReadsFixtures.read_raw_json_fixture("response/checkout_conversion"),
                "/metrics/checkout-conversion?from=2025-09-01&to=2025-09-05",
                MetricsCheckoutConversion,
            ),
        ],
        ids=[
            "Get monthly recurring revenue",
            "Get monthly recurring revenue change",
            "Get active subscribers",
            "Get revenue",
            "Get refunds",
            "Get chargebacks",
            "Get checkout conversion",
        ],
    )
    def test_metrics_returns_expected_response(
        self,
        test_client,
        mock_requests,
        method,
        operation,
        expected_response_body,
        expected_url,
        expected_entity_type,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        response = getattr(test_client.client.metrics, method)(operation)
        response_json = test_client.client.metrics.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, expected_entity_type)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url, "The URL does not match the expected URL"
        assert (
            loads(dumps(response, cls=PayloadEncoder)) == loads(str(expected_response_body))["data"]
        ), "The metrics response object doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"
