from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Report                       import Report
from paddle_billing_python_sdk.Entities.ReportCSV                    import ReportCSV
from paddle_billing_python_sdk.Entities.Collections.Paginator        import Paginator
from paddle_billing_python_sdk.Entities.Collections.ReportCollection import ReportCollection

from paddle_billing_python_sdk.Resources.Reports.Operations.CreateReport import CreateReport
from paddle_billing_python_sdk.Resources.Reports.Operations.ListReports  import ListReports


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class ReportsClient:
    def __init__(self, client: 'Client'):
        self.client = client


    def list(self, operation: ListReports = None) -> ReportCollection:
        if operation is None:
            operation = ListReports()

        response = self.client.get_raw('/reports', operation.get_parameters())
        parser   = ResponseParser(response)

        return ReportCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), ReportCollection)
        )


    def get(self, report_id: str) -> Report:
        response   = self.client.get_raw(f"/reports/{report_id}")
        parser     = ResponseParser(response)

        return Report.from_dict(parser.get_data())


    def get_report_csv(self, report_id: str) -> ReportCSV:
        response = self.client.get_raw(f"/reports/{report_id}/download-url")
        parser   = ResponseParser(response)

        return ReportCSV.from_dict(parser.get_data())


    def create(self, operation: CreateReport) -> Report:
        response = self.client.post_raw('/reports', operation.get_parameters())
        parser   = ResponseParser(response)

        return Report.from_dict(parser.get_data())
