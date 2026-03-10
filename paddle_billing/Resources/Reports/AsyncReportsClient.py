# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Reports/ReportsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Report import Report
from paddle_billing.Entities.ReportCSV import ReportCSV
from paddle_billing.Entities.Collections import ReportCollection

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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return ReportCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), ReportCollection)
            )
        return await self.client._get("/reports", operation.get_parameters(), parse)

    async def get(self, report_id: str) -> Report:
        def parse(response):
            self.response = response
            return Report.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/reports/{report_id}", None, parse)

    async def get_report_csv(self, report_id: str) -> ReportCSV:
        def parse(response):
            self.response = response
            return ReportCSV.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/reports/{report_id}/download-url", None, parse)

    async def create(self, operation: CreateReport) -> Report:
        def parse(response):
            self.response = response
            return Report.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/reports", operation, parse)
