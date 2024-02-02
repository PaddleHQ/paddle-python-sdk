from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Business    import Business
from paddle_billing.Entities.Collections import Paginator,  BusinessCollection
from paddle_billing.Entities.Shared      import Status

from paddle_billing.Resources.Businesses.Operations import CreateBusiness, ListBusinesses, UpdateBusiness

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client import Client


class BusinessesClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, customer_id: str, operation: ListBusinesses = None) -> BusinessCollection:
        if operation is None:
            operation = ListBusinesses()

        self.response = self.client.get_raw(f"/customers/{customer_id}/businesses", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return BusinessCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), BusinessCollection)
        )


    def get(self, customer_id: str, business_id: str) -> Business:
        self.response = self.client.get_raw(f"/customers/{customer_id}/businesses/{business_id}")
        parser        = ResponseParser(self.response)

        return Business.from_dict(parser.get_data())


    def create(self, customer_id: str, operation: CreateBusiness) -> Business:
        self.response = self.client.post_raw(f"/customers/{customer_id}/businesses", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Business.from_dict(parser.get_data())


    def update(self, customer_id: str, business_id: str, operation: UpdateBusiness) -> Business:
        self.response = self.client.patch_raw(
            f"/customers/{customer_id}/businesses/{business_id}",
            operation.get_parameters()
        )
        parser = ResponseParser(self.response)

        return Business.from_dict(parser.get_data())


    def archive(self, customer_id: str, business_id: str) -> Business:
        return self.update(customer_id, business_id, UpdateBusiness(status=Status.Archived))
