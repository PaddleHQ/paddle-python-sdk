from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Business                       import Business
from paddle_billing_python_sdk.Entities.Collections.Paginator          import Paginator
from paddle_billing_python_sdk.Entities.Collections.BusinessCollection import BusinessCollection
from paddle_billing_python_sdk.Entities.Shared.Status                  import Status

from paddle_billing_python_sdk.Resources.Businesses.Operations.CreateBusiness import CreateBusiness
from paddle_billing_python_sdk.Resources.Businesses.Operations.ListBusinesses import ListBusinesses
from paddle_billing_python_sdk.Resources.Businesses.Operations.UpdateBusiness import UpdateBusiness


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class BusinessesClient:
    def __init__(self, client: 'Client'):
        self.client = client


    def list(self, customer_id: str, operation: ListBusinesses = None) -> BusinessCollection:
        if operation is None:
            operation = ListBusinesses()

        response = self.client.get_raw(f"/customers/{customer_id}/businesses", operation.get_parameters())
        parser   = ResponseParser(response)

        return BusinessCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), BusinessCollection)
        )


    def get(self, customer_id: str, business_id: str) -> Business:
        response = self.client.get_raw(f"/customers/{customer_id}/businesses/{business_id}")
        parser   = ResponseParser(response)

        return Business.from_dict(parser.get_data())


    def create(self, customer_id: str, operation: CreateBusiness) -> Business:
        response = self.client.post_raw(f"/customers/{customer_id}/businesses", operation.get_parameters())
        parser   = ResponseParser(response)

        return Business.from_dict(parser.get_data())


    def update(self, customer_id: str, business_id: str, operation: UpdateBusiness) -> Business:
        response = self.client.patch_raw(
            f"/customers/{customer_id}/businesses/{business_id}",
            operation.get_parameters()
        )
        parser = ResponseParser(response)

        return Business.from_dict(parser.get_data())


    def archive(self, customer_id: str, business_id: str) -> Business:
        return self.update(customer_id, business_id, UpdateBusiness(status=Status.Archived))
