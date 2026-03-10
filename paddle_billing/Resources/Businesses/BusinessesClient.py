from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Business import Business
from paddle_billing.Entities.Collections import BusinessCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Resources.Businesses.Operations import CreateBusiness, ListBusinesses, UpdateBusiness

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class BusinessesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, customer_id: str, operation: ListBusinesses | None = None) -> BusinessCollection:
        if operation is None:
            operation = ListBusinesses()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return BusinessCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), BusinessCollection)
            )
        return self.client._get(f"/customers/{customer_id}/businesses", operation.get_parameters(), parse)

    def get(self, customer_id: str, business_id: str) -> Business:
        def parse(response):
            self.response = response
            return Business.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/customers/{customer_id}/businesses/{business_id}", None, parse)

    def create(self, customer_id: str, operation: CreateBusiness) -> Business:
        def parse(response):
            self.response = response
            return Business.from_dict(ResponseParser(response).get_dict())
        return self.client._post(f"/customers/{customer_id}/businesses", operation, parse)

    def update(self, customer_id: str, business_id: str, operation: UpdateBusiness) -> Business:
        def parse(response):
            self.response = response
            return Business.from_dict(ResponseParser(response).get_dict())
        return self.client._patch(f"/customers/{customer_id}/businesses/{business_id}", operation, parse)

    def archive(self, customer_id: str, business_id: str) -> Business:
        return self.update(customer_id, business_id, UpdateBusiness(status=Status.Archived))
