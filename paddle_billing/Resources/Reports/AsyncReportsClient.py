from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Report import Report
from paddle_billing.Entities.ReportCSV import ReportCSV
from paddle_billing.Entities.Collections import AsyncPaginator, ReportCollection

from paddle_billing.Resources.Reports.Operations import CreateReport, ListReports

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncReportsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListReports | None = None) -> ReportCollection:
        if operation is None:
            operation = ListReports()

        self.response = await self.client.get_raw("/reports", operation.get_parameters())
        parser = ResponseParser(self.response)

        return ReportCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), ReportCollection)
        )

    async def get(self, report_id: str) -> Report:
        self.response = await self.client.get_raw(f"/reports/{report_id}")
        parser = ResponseParser(self.response)

        return Report.from_dict(parser.get_dict())

    async def get_report_csv(self, report_id: str) -> ReportCSV:
        self.response = await self.client.get_raw(f"/reports/{report_id}/download-url")
        parser = ResponseParser(self.response)

        return ReportCSV.from_dict(parser.get_dict())

    async def create(self, operation: CreateReport) -> Report:
        self.response = await self.client.post_raw("/reports", operation)
        parser = ResponseParser(self.response)

        return Report.from_dict(parser.get_dict())
