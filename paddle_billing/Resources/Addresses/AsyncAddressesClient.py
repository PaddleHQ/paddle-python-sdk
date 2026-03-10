from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Address import Address
from paddle_billing.Entities.Collections import AsyncPaginator, AddressCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Resources.Addresses.Operations import CreateAddress, ListAddresses, UpdateAddress

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncAddressesClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, customer_id: str, operation: ListAddresses | None = None) -> AddressCollection:
        if operation is None:
            operation = ListAddresses()

        self.response = await self.client.get_raw(f"/customers/{customer_id}/addresses", operation.get_parameters())
        parser = ResponseParser(self.response)

        return AddressCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), AddressCollection)
        )

    async def get(self, customer_id: str, address_id: str) -> Address:
        self.response = await self.client.get_raw(f"/customers/{customer_id}/addresses/{address_id}")
        parser = ResponseParser(self.response)

        return Address.from_dict(parser.get_dict())

    async def create(self, customer_id: str, operation: CreateAddress) -> Address:
        self.response = await self.client.post_raw(f"/customers/{customer_id}/addresses", operation)
        parser = ResponseParser(self.response)

        return Address.from_dict(parser.get_dict())

    async def update(self, customer_id: str, address_id: str, operation: UpdateAddress) -> Address:
        self.response = await self.client.patch_raw(f"/customers/{customer_id}/addresses/{address_id}", operation)
        parser = ResponseParser(self.response)

        return Address.from_dict(parser.get_dict())

    async def archive(self, customer_id: str, address_id: str) -> Address:
        return await self.update(customer_id, address_id, UpdateAddress(status=Status.Archived))
