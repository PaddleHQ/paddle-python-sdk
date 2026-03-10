from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Business import Business
from paddle_billing.Entities.Collections import AsyncPaginator, BusinessCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Resources.Businesses.Operations import CreateBusiness, ListBusinesses, UpdateBusiness

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncBusinessesClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, customer_id: str, operation: ListBusinesses | None = None) -> BusinessCollection:
        if operation is None:
            operation = ListBusinesses()

        self.response = await self.client.get_raw(f"/customers/{customer_id}/businesses", operation.get_parameters())
        parser = ResponseParser(self.response)

        return BusinessCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), BusinessCollection)
        )

    async def get(self, customer_id: str, business_id: str) -> Business:
        self.response = await self.client.get_raw(f"/customers/{customer_id}/businesses/{business_id}")
        parser = ResponseParser(self.response)

        return Business.from_dict(parser.get_dict())

    async def create(self, customer_id: str, operation: CreateBusiness) -> Business:
        self.response = await self.client.post_raw(f"/customers/{customer_id}/businesses", operation)
        parser = ResponseParser(self.response)

        return Business.from_dict(parser.get_dict())

    async def update(self, customer_id: str, business_id: str, operation: UpdateBusiness) -> Business:
        self.response = await self.client.patch_raw(f"/customers/{customer_id}/businesses/{business_id}", operation)
        parser = ResponseParser(self.response)

        return Business.from_dict(parser.get_dict())

    async def archive(self, customer_id: str, business_id: str) -> Business:
        return await self.update(customer_id, business_id, UpdateBusiness(status=Status.Archived))
