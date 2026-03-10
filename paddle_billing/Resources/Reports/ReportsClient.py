from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Report import Report
from paddle_billing.Entities.ReportCSV import ReportCSV
from paddle_billing.Entities.Collections import ReportCollection

from paddle_billing.Resources.Reports.Operations import CreateReport, ListReports

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class ReportsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListReports | None = None) -> ReportCollection:
        if operation is None:
            operation = ListReports()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return ReportCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), ReportCollection)
            )
        return self.client._get("/reports", operation.get_parameters(), parse)

    def get(self, report_id: str) -> Report:
        def parse(response):
            self.response = response
            return Report.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/reports/{report_id}", None, parse)

    def get_report_csv(self, report_id: str) -> ReportCSV:
        def parse(response):
            self.response = response
            return ReportCSV.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/reports/{report_id}/download-url", None, parse)

    def create(self, operation: CreateReport) -> Report:
        def parse(response):
            self.response = response
            return Report.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/reports", operation, parse)
