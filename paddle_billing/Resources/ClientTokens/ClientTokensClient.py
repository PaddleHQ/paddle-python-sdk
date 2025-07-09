from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import Paginator, ClientTokenCollection
from paddle_billing.Entities.ClientToken import ClientToken
from paddle_billing.Entities.ClientTokens import ClientTokenStatus

from paddle_billing.Resources.ClientTokens.Operations import CreateClientToken, ListClientTokens, UpdateClientToken

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class ClientTokensClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListClientTokens | None = None) -> ClientTokenCollection:
        if operation is None:
            operation = ListClientTokens()

        self.response = self.client.get_raw("/client-tokens", operation.get_parameters())
        parser = ResponseParser(self.response)

        return ClientTokenCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), ClientTokenCollection)
        )

    def get(self, client_token_id: str) -> ClientToken:
        self.response = self.client.get_raw(f"/client-tokens/{client_token_id}")
        parser = ResponseParser(self.response)

        return ClientToken.from_dict(parser.get_dict())

    def create(self, operation: CreateClientToken) -> ClientToken:
        self.response = self.client.post_raw("/client-tokens", operation)
        parser = ResponseParser(self.response)

        return ClientToken.from_dict(parser.get_dict())

    def update(self, client_token_id: str, operation: UpdateClientToken) -> ClientToken:
        self.response = self.client.patch_raw(f"/client-tokens/{client_token_id}", operation)
        parser = ResponseParser(self.response)

        return ClientToken.from_dict(parser.get_dict())

    def revoke(self, client_token_id: str) -> ClientToken:
        return self.update(client_token_id, UpdateClientToken(status=ClientTokenStatus.Revoked))
