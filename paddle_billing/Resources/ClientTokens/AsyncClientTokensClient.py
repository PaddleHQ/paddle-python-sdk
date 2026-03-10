from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, ClientTokenCollection
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

        self.response = await self.client.get_raw("/client-tokens", operation.get_parameters())
        parser = ResponseParser(self.response)

        return ClientTokenCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), ClientTokenCollection)
        )

    async def get(self, client_token_id: str) -> ClientToken:
        self.response = await self.client.get_raw(f"/client-tokens/{client_token_id}")
        parser = ResponseParser(self.response)

        return ClientToken.from_dict(parser.get_dict())

    async def create(self, operation: CreateClientToken) -> ClientToken:
        self.response = await self.client.post_raw("/client-tokens", operation)
        parser = ResponseParser(self.response)

        return ClientToken.from_dict(parser.get_dict())

    async def update(self, client_token_id: str, operation: UpdateClientToken) -> ClientToken:
        self.response = await self.client.patch_raw(f"/client-tokens/{client_token_id}", operation)
        parser = ResponseParser(self.response)

        return ClientToken.from_dict(parser.get_dict())

    async def revoke(self, client_token_id: str) -> ClientToken:
        return await self.update(client_token_id, UpdateClientToken(status=ClientTokenStatus.Revoked))
