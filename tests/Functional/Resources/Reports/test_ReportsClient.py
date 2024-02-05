from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import ReportCollection
from paddle_billing.Entities.Report      import Report
from paddle_billing.Entities.ReportCSV   import ReportCSV
from paddle_billing.Entities.Reports     import ReportFilter, ReportFilterName, ReportFilterOperator, ReportStatus, ReportType

from paddle_billing.Resources.Reports.Operations import CreateReport, ListReports
from paddle_billing.Resources.Shared.Operations  import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestReportsClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                CreateReport(type=ReportType.Transactions),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/reports',
            ), (
                CreateReport(
                    type    = ReportType.Transactions,
                    filters = [ReportFilter(name=ReportFilterName.UpdatedAt, operator=ReportFilterOperator.Lt, value='2023-12-30')],
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/reports',
            ),
        ],
        ids=[
            "Create report with basic data",
            "Create report with filters",
        ],
    )
    def test_create_report_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.reports.create(operation)
        response_json = test_client.client.reports.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Report)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                ListReports(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/reports',
            ), (
                ListReports(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/reports?order_by=id[asc]&per_page=50',
            ), (
                ListReports(Pager(after='rep_01hhq4c3b03g3x2kpkj8aecjv6')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/reports?after=rep_01hhq4c3b03g3x2kpkj8aecjv6&order_by=id[asc]&per_page=50',
            ), (
                ListReports(statuses=[ReportStatus.Ready]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/reports?status=ready',
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

        response     = test_client.client.reports.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, ReportCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'report_id, expected_response_status, expected_response_body, expected_url',
        [(
            'rep_01hhq4c3b03g3x2kpkj8aecjv6',
            200,
            ReadsFixtures.read_raw_json_fixture('response/full_entity'),
            '/reports/rep_01hhq4c3b03g3x2kpkj8aecjv6',
        )],
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

        response      = test_client.client.reports.get(report_id)
        response_json = test_client.client.reports.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Report)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"


    @mark.parametrize(
        'report_id, expected_response_status, expected_response_body, expected_url',
        [(
            'rep_01hhq4c3b03g3x2kpkj8aecjv6',
            200,
            ReadsFixtures.read_raw_json_fixture('response/report_csv_entity'),
            '/reports/rep_01hhq4c3b03g3x2kpkj8aecjv6/download-url',
        )],
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

        response      = test_client.client.reports.get_report_csv(report_id)
        response_json = test_client.client.reports.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, ReportCSV)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
