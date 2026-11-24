from requests import Response

from paddle_billing.ResponseParser import ResponseParser as ResponseParser

from paddle_billing.Entities.Business import Business as Business
from paddle_billing.Entities.Collections import Paginator as Paginator, BusinessCollection as BusinessCollection
from paddle_billing.Entities.Shared import Status as Status

from paddle_billing.Resources.Businesses.Operations import (
    CreateBusiness as CreateBusiness,
    ListBusinesses as ListBusinesses,
    UpdateBusiness as UpdateBusiness,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class BusinessesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response: Response | None = None

    def list(self, customer_id: str, operation: ListBusinesses | None = None) -> BusinessCollection:
        if operation is None:
            operation = ListBusinesses()

        self.response = self.client.get_raw(f"/customers/{customer_id}/businesses", operation.get_parameters())
        parser = ResponseParser(self.response)

        return BusinessCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), BusinessCollection)
        )

    def get(self, customer_id: str, business_id: str) -> Business:
        self.response = self.client.get_raw(f"/customers/{customer_id}/businesses/{business_id}")
        parser = ResponseParser(self.response)

        return Business.from_dict(parser.get_dict())

    def create(self, customer_id: str, operation: CreateBusiness) -> Business:
        self.response = self.client.post_raw(f"/customers/{customer_id}/businesses", operation)
        parser = ResponseParser(self.response)

        return Business.from_dict(parser.get_dict())

    def update(self, customer_id: str, business_id: str, operation: UpdateBusiness) -> Business:
        self.response = self.client.patch_raw(f"/customers/{customer_id}/businesses/{business_id}", operation)
        parser = ResponseParser(self.response)

        return Business.from_dict(parser.get_dict())

    def archive(self, customer_id: str, business_id: str) -> Business:
        return self.update(customer_id, business_id, UpdateBusiness(status=Status.Archived))
