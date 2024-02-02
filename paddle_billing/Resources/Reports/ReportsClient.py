from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Report      import Report
from paddle_billing.Entities.ReportCSV   import ReportCSV
from paddle_billing.Entities.Collections import Paginator, ReportCollection

from paddle_billing.Resources.Reports.Operations import CreateReport, ListReports

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client import Client


class ReportsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListReports = None) -> ReportCollection:
        if operation is None:
            operation = ListReports()

        self.response = self.client.get_raw('/reports', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return ReportCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), ReportCollection)
        )


    def get(self, report_id: str) -> Report:
        self.response   = self.client.get_raw(f"/reports/{report_id}")
        parser          = ResponseParser(self.response)

        return Report.from_dict(parser.get_data())


    def get_report_csv(self, report_id: str) -> ReportCSV:
        self.response = self.client.get_raw(f"/reports/{report_id}/download-url")
        parser        = ResponseParser(self.response)

        return ReportCSV.from_dict(parser.get_data())


    def create(self, operation: CreateReport) -> Report:
        self.response = self.client.post_raw('/reports', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Report.from_dict(parser.get_data())
