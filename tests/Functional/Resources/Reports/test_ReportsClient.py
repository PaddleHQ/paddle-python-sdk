from json import loads
from pytest import mark, raises
from urllib.parse import unquote

from paddle_billing.Entities.Collections import ReportCollection
from paddle_billing.Entities.Report import Report
from paddle_billing.Entities.ReportCSV import ReportCSV
from paddle_billing.Entities.Reports import (
    AdjustmentsReportType,
    DiscountsReportType,
    ProductsPricesReportType,
    ReportFilter,
    ReportFilterName,
    ReportFilterOperator,
    ReportStatus,
    TransactionsReportType,
)

from paddle_billing.Entities.DateTime import DateTime

from paddle_billing.Resources.Reports.Operations.Filters import (
    AdjustmentActionFilter,
    AdjustmentStatusFilter,
    CollectionModeFilter,
    CurrencyCodeFilter,
    DiscountStatusFilter,
    DiscountTypeFilter,
    PriceStatusFilter,
    PriceTypeFilter,
    PriceUpdatedAtFilter,
    ProductStatusFilter,
    ProductTypeFilter,
    ProductUpdatedAtFilter,
    TransactionOriginFilter,
    TransactionStatusFilter,
    UpdatedAtFilter,
)

from paddle_billing.Entities.Shared import (
    AdjustmentStatus,
    Action,
    CatalogType,
    CollectionMode,
    CurrencyCode,
    TransactionOrigin,
    TransactionStatus,
    Status,
)

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Entities.Discounts import (
    DiscountStatus,
    DiscountType,
)

from paddle_billing.Resources.Reports.Operations import (
    CreateAdjustmentsReport,
    CreateDiscountsReport,
    CreateProductsAndPricesReport,
    CreateTransactionsReport,
    ListReports,
)

from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


class TestReportsClient:
    @mark.parametrize(
        "operation, expected_request_body, expected_report_type",
        [
            (
                CreateTransactionsReport(type=TransactionsReportType.TransactionLineItems),
                ReadsFixtures.read_raw_json_fixture("request/create_transaction_basic"),
                TransactionsReportType,
            ),
            (
                CreateTransactionsReport(
                    type=TransactionsReportType.Transactions,
                    filters=[
                        CollectionModeFilter([CollectionMode.Automatic]),
                        CurrencyCodeFilter([CurrencyCode.USD]),
                        TransactionOriginFilter([TransactionOrigin.SubscriptionCharge]),
                        TransactionStatusFilter([TransactionStatus.Completed]),
                        UpdatedAtFilter.gte(DateTime("2023-12-30")),
                        UpdatedAtFilter.lt(DateTime("2024-12-30T12:30:01.123456Z")),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_transaction_full"),
                TransactionsReportType,
            ),
            (
                CreateAdjustmentsReport(type=AdjustmentsReportType.AdjustmentLineItems),
                ReadsFixtures.read_raw_json_fixture("request/create_adjustment_basic"),
                AdjustmentsReportType,
            ),
            (
                CreateAdjustmentsReport(
                    type=AdjustmentsReportType.Adjustments,
                    filters=[
                        AdjustmentActionFilter([Action.Chargeback]),
                        AdjustmentStatusFilter([AdjustmentStatus.Approved]),
                        CurrencyCodeFilter([CurrencyCode.USD]),
                        UpdatedAtFilter.gte(DateTime("2023-12-30")),
                        UpdatedAtFilter.lt(DateTime("2024-12-30T12:30:01.123456Z")),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_adjustment_full"),
                AdjustmentsReportType,
            ),
            (
                CreateDiscountsReport(
                    type=DiscountsReportType.Discounts,
                    filters=[
                        DiscountStatusFilter([DiscountStatus.Active]),
                        DiscountTypeFilter([DiscountType.Flat]),
                        UpdatedAtFilter.gte(DateTime("2023-12-30")),
                        UpdatedAtFilter.lt(DateTime("2024-12-30T12:30:01.123456Z")),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_discount_full"),
                DiscountsReportType,
            ),
            (
                CreateProductsAndPricesReport(
                    type=ProductsPricesReportType.ProductsPrices,
                    filters=[
                        ProductStatusFilter([Status.Active]),
                        ProductTypeFilter([CatalogType.Standard, CatalogType.Custom]),
                        ProductUpdatedAtFilter.gte(DateTime("2023-12-30")),
                        ProductUpdatedAtFilter.lt(DateTime("2024-12-30T12:30:01.123456Z")),
                        PriceStatusFilter([Status.Active]),
                        PriceTypeFilter([CatalogType.Standard, CatalogType.Custom]),
                        PriceUpdatedAtFilter.gte(DateTime("2023-12-30")),
                        PriceUpdatedAtFilter.lt(DateTime("2024-12-30T12:30:01.123456Z")),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_products_prices_full"),
                ProductsPricesReportType,
            ),
        ],
        ids=[
            "Create transaction report with basic data",
            "Create transaction report with filters",
            "Create adjustment report with basic data",
            "Create adjustment report with filters",
            "Create discount report with filters",
            "Create products and prices report with filters",
        ],
    )
    def test_create_report_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_report_type,
    ):
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")
        expected_url = f"{test_client.base_url}/reports"

        mock_requests.post(
            expected_url,
            status_code=200,
            text=expected_response_body,
        )

        assert isinstance(operation.type, expected_report_type)

        response = test_client.client.reports.create(operation)
        response_json = test_client.client.reports.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Report)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    def test_create_report_validates_allowed_filters(self):
        with raises(InvalidArgumentException) as exception_info:
            CreateTransactionsReport(
                type=TransactionsReportType.Transactions,
                filters=[
                    AdjustmentActionFilter([Action.Chargeback]),
                    PriceUpdatedAtFilter.gte("2023-12-30"),
                ],
            )

        assert (
            str(exception_info.value)
            == "Expected 'filters' to only contain types 'CollectionModeFilter', 'CurrencyCodeFilter', 'TransactionOriginFilter', 'TransactionStatusFilter', 'UpdatedAtFilter' ('AdjustmentActionFilter', 'PriceUpdatedAtFilter' given)"
        )

    @mark.parametrize(
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                ListReports(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/reports",
            ),
            (
                ListReports(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/reports?order_by=id[asc]&per_page=50",
            ),
            (
                ListReports(Pager(after="rep_01hhq4c3b03g3x2kpkj8aecjv6")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/reports?after=rep_01hhq4c3b03g3x2kpkj8aecjv6&order_by=id[asc]&per_page=50",
            ),
            (
                ListReports(statuses=[ReportStatus.Ready]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/reports?status=ready",
            ),
        ],
        ids=[
            "List reports without pagination",
            "List reports with default pagination",
            "List paginated reports after specified report id",
            "List reports filtered by status",
        ],
    )
    def test_list_reports_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status)

        response = test_client.client.reports.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, ReportCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    @mark.parametrize(
        "report_id, expected_response_status, expected_response_body, expected_url",
        [
            (
                "rep_01hhq4c3b03g3x2kpkj8aecjv6",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/reports/rep_01hhq4c3b03g3x2kpkj8aecjv6",
            )
        ],
        ids=["Get a report by its id"],
    )
    def test_get_report_returns_expected_response(
        self,
        test_client,
        mock_requests,
        report_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.reports.get(report_id)
        response_json = test_client.client.reports.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, Report)

        assert len(response.filters) == 1

        filter = response.filters[0]

        assert isinstance(filter, ReportFilter)
        assert filter.name == ReportFilterName.UpdatedAt
        assert filter.operator == ReportFilterOperator.Lt
        assert filter.value == "2023-12-30"

        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

    @mark.parametrize(
        "report_id, expected_response_status, expected_response_body, expected_url",
        [
            (
                "rep_01hhq4c3b03g3x2kpkj8aecjv6",
                200,
                ReadsFixtures.read_raw_json_fixture("response/report_csv_entity"),
                "/reports/rep_01hhq4c3b03g3x2kpkj8aecjv6/download-url",
            )
        ],
        ids=["Get a report csv by its id"],
    )
    def test_get_report_csv_returns_expected_response(
        self,
        test_client,
        mock_requests,
        report_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.reports.get_report_csv(report_id)
        response_json = test_client.client.reports.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, ReportCSV)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
