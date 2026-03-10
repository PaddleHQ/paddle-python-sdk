# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Addresses/AddressesClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Address import Address
from paddle_billing.Entities.Collections import AddressCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return AddressCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), AddressCollection)
            )
        return await self.client._get(f"/customers/{customer_id}/addresses", operation.get_parameters(), parse)

    async def get(self, customer_id: str, address_id: str) -> Address:
        def parse(response):
            self.response = response
            return Address.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/customers/{customer_id}/addresses/{address_id}", None, parse)

    async def create(self, customer_id: str, operation: CreateAddress) -> Address:
        def parse(response):
            self.response = response
            return Address.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/customers/{customer_id}/addresses", operation, parse)

    async def update(self, customer_id: str, address_id: str, operation: UpdateAddress) -> Address:
        def parse(response):
            self.response = response
            return Address.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/customers/{customer_id}/addresses/{address_id}", operation, parse)

    async def archive(self, customer_id: str, address_id: str) -> Address:
        return await self.update(customer_id, address_id, UpdateAddress(status=Status.Archived))
