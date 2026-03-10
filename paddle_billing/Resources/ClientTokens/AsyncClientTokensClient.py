# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/ClientTokens/ClientTokensClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import ClientTokenCollection
from paddle_billing.Entities.ClientToken import ClientToken
from paddle_billing.Entities.ClientTokens import ClientTokenStatus

from paddle_billing.Resources.ClientTokens.Operations import CreateClientToken, ListClientTokens, UpdateClientToken

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncClientTokensClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListClientTokens | None = None) -> ClientTokenCollection:
        if operation is None:
            operation = ListClientTokens()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return ClientTokenCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), ClientTokenCollection)
            )
        return await self.client._get("/client-tokens", operation.get_parameters(), parse)

    async def get(self, client_token_id: str) -> ClientToken:
        def parse(response):
            self.response = response
            return ClientToken.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/client-tokens/{client_token_id}", None, parse)

    async def create(self, operation: CreateClientToken) -> ClientToken:
        def parse(response):
            self.response = response
            return ClientToken.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/client-tokens", operation, parse)

    async def update(self, client_token_id: str, operation: UpdateClientToken) -> ClientToken:
        def parse(response):
            self.response = response
            return ClientToken.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/client-tokens/{client_token_id}", operation, parse)

    async def revoke(self, client_token_id: str) -> ClientToken:
        return await self.update(client_token_id, UpdateClientToken(status=ClientTokenStatus.Revoked))
