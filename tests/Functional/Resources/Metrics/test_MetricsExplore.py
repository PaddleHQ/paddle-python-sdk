from datetime import date, datetime, timezone
from json import loads

from paddle_billing.Entities.Metrics import (
    MetricEntity,
    MetricEntityDefinition,
    MetricsAggregation,
    MetricsBucketInterval,
    MetricsExploreResponse,
    MetricsFieldType,
    MetricsFilterOperator,
    MetricsSortDirection,
)
from paddle_billing.Entities.Shared import CurrencyCode
from paddle_billing.Resources.Metrics.Operations import (
    ExploreFilter,
    ExploreMeasure,
    ExploreOrderBy,
    ListExploreMetricEntities,
    RunExploreMetricsQuery,
)

from tests.Utils.ReadsFixture import ReadsFixtures

FIRST_CURSOR = (
    "eyJ2IjoxLCJxaWQiOiIwMWpuOHg0azJwN3E5ciIsIm9mZiI6NSwicWgiOiJzaGEyNTY6OWYyYzRkMWUiLCJleHAiOjE3ODU1Njc2MDB9"
)


class TestMetricsExploreEntities:
    def test_list_explore_entities_returns_all_entities(self, test_client, mock_requests):
        body = ReadsFixtures.read_raw_json_fixture("response/explore_entities")
        url = f"{test_client.base_url}/metrics/explore/entities"
        mock_requests.get(url, status_code=200, text=body)

        entities = test_client.client.metrics.list_explore_entities()

        assert mock_requests.last_request.method == "GET"
        assert mock_requests.last_request.url == url
        assert len(entities) == 1
        entity = entities[0]
        assert isinstance(entity, MetricEntityDefinition)
        assert entity.entity == MetricEntity.Subscriptions
        assert entity.time_dimension.intervals == [MetricsBucketInterval.Month]
        assert entity.time_dimension.max_lookback_days == 1096
        assert [dimension.name for dimension in entity.dimensions] == [
            "product",
            "country",
            "billing_cycle",
            "subscription_activity",
        ]
        assert entity.dimensions[0].type == MetricsFieldType.String
        assert entity.dimensions[0].filter_ops == [MetricsFilterOperator.In]
        assert entity.dimensions[0].multi_valued is False
        assert entity.measures[0].name == "mrr"
        assert entity.measures[0].type == MetricsFieldType.Currency
        assert entity.measures[0].aggs is None

    def test_list_explore_entities_filters_by_entity(self, test_client, mock_requests):
        body = ReadsFixtures.read_raw_json_fixture("response/explore_entities")
        url = f"{test_client.base_url}/metrics/explore/entities?entity=subscriptions"
        mock_requests.get(url, status_code=200, text=body)

        entities = test_client.client.metrics.list_explore_entities(
            ListExploreMetricEntities(entity=MetricEntity.Subscriptions)
        )

        assert mock_requests.last_request.url == url
        assert len(entities) == 1

    def test_measure_aggs_are_parsed(self, test_client, mock_requests):
        body = '{"data":[{"entity":"checkouts","time_dimension":{"intervals":["day","week"],"max_lookback_days":90},'
        body += '"dimensions":[],"measures":[{"name":"gross","type":"currency","aggs":["sum","count"]}]}],"meta":{}}'
        mock_requests.get(f"{test_client.base_url}/metrics/explore/entities", status_code=200, text=body)

        entity = test_client.client.metrics.list_explore_entities()[0]

        assert entity.measures[0].aggs == [MetricsAggregation.Sum, MetricsAggregation.Count]
        assert entity.time_dimension.intervals == [MetricsBucketInterval.Day, MetricsBucketInterval.Week]


class TestMetricsExploreQuery:
    def test_run_explore_query_sends_full_body_and_parses_response(self, test_client, mock_requests):
        body = ReadsFixtures.read_raw_json_fixture("response/explore")
        url = f"{test_client.base_url}/metrics/explore"
        mock_requests.post(url, status_code=200, text=body)

        operation = RunExploreMetricsQuery(
            entity=MetricEntity.TransactionsCompleted,
            date_from=datetime(2026, 5, 1, tzinfo=timezone.utc),
            date_to=date(2026, 8, 1),
            measures=[ExploreMeasure(field="gross_revenue", agg=MetricsAggregation.Sum), ExploreMeasure(field="count")],
            interval=MetricsBucketInterval.Month,
            dimensions=["product"],
            filters=[ExploreFilter(field="country", op=MetricsFilterOperator.In, value=["US", "GB"])],
            order_by=[ExploreOrderBy(field="gross_revenue", dir=MetricsSortDirection.Desc)],
            per_page=5,
        )

        response = test_client.client.metrics.run_explore_query(operation)

        request = mock_requests.last_request
        assert request.method == "POST"
        assert request.url == url
        assert loads(request.text) == {
            "entity": "transactions.completed",
            "from": "2026-05-01T00:00:00.000000Z",
            "to": "2026-08-01",
            "measures": [{"field": "gross_revenue", "agg": "sum"}, {"field": "count"}],
            "interval": "month",
            "dimensions": ["product"],
            "filters": [{"field": "country", "op": "in", "value": ["US", "GB"]}],
            "order_by": [{"field": "gross_revenue", "dir": "desc"}],
            "per_page": 5,
        }

        assert isinstance(response, MetricsExploreResponse)
        data = response.data
        assert data.entity == MetricEntity.TransactionsCompleted
        assert data.interval == MetricsBucketInterval.Month
        assert data.currency_code == CurrencyCode.USD
        assert data.starts_at == datetime(2026, 5, 1, tzinfo=timezone.utc)
        assert data.ends_at == datetime(2026, 8, 1, tzinfo=timezone.utc)
        assert data.updated_at == datetime(2026, 8, 1, 3, tzinfo=timezone.utc)
        assert data.fields.dimensions[0].name == "product"
        assert data.fields.dimensions[0].type == MetricsFieldType.String
        assert data.fields.measures[0].name == "sum_gross_revenue"
        assert data.fields.measures[0].type == MetricsFieldType.Currency
        assert data.fields.measures[0].field == "gross_revenue"
        assert data.fields.measures[0].agg == MetricsAggregation.Sum
        assert len(data.series) == 1
        assert data.series[0].dimensions == {"product": "pro_01h1vjfevh5etwq3rb416a23h2"}
        assert [point.timestamp for point in data.series[0].timeseries] == ["2026-05-01", "2026-06-01", "2026-07-01"]
        assert data.series[0].timeseries[2].measures == {"sum_gross_revenue": "142000"}

        pagination = response.meta.pagination
        assert response.meta.request_id == "b93d9c94-c28f-4e5d-af2e-044854d7afe8"
        assert pagination.per_page == 5
        assert pagination.has_more is True
        assert pagination.estimated_total == 42
        assert pagination.next == f"https://api.paddle.com/metrics/explore?after={FIRST_CURSOR}"
        assert response.has_more is True
        assert response.next_cursor == FIRST_CURSOR

    def test_run_explore_query_minimal_body_omits_optional_fields(self, test_client, mock_requests):
        body = ReadsFixtures.read_raw_json_fixture("response/explore")
        mock_requests.post(f"{test_client.base_url}/metrics/explore", status_code=200, text=body)

        test_client.client.metrics.run_explore_query(
            RunExploreMetricsQuery(
                entity=MetricEntity.Checkouts,
                date_from="2026-05-01",
                date_to="2026-08-01",
                measures=[ExploreMeasure(field="count")],
            )
        )

        assert loads(mock_requests.last_request.text) == {
            "entity": "checkouts",
            "from": "2026-05-01",
            "to": "2026-08-01",
            "measures": [{"field": "count"}],
        }

    def test_run_explore_query_follows_next_cursor(self, test_client, mock_requests):
        first_page = ReadsFixtures.read_raw_json_fixture("response/explore")
        last_page = ReadsFixtures.read_raw_json_fixture("response/explore_last_page")
        url = f"{test_client.base_url}/metrics/explore"
        mock_requests.post(url, status_code=200, text=first_page)
        mock_requests.post(f"{url}?after={FIRST_CURSOR}", status_code=200, text=last_page)

        operation = RunExploreMetricsQuery(
            entity=MetricEntity.TransactionsCompleted,
            date_from="2026-05-01",
            date_to="2026-08-01",
            measures=[ExploreMeasure(field="gross_revenue", agg=MetricsAggregation.Sum)],
            dimensions=["product"],
        )

        first = test_client.client.metrics.run_explore_query(operation)
        assert mock_requests.last_request.url == url

        second = test_client.client.metrics.run_explore_query(operation, after=first.next_cursor)

        assert mock_requests.last_request.url == f"{url}?after={FIRST_CURSOR}"
        assert loads(mock_requests.last_request.text)["dimensions"] == ["product"]
        assert second.data.series[0].dimensions == {"product": "pro_01h1vjfevh5etwq3rb416a23h3"}
        assert second.has_more is False
        assert second.next_cursor is None
