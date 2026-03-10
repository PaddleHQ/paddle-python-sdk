from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import ClientTokenCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return ClientTokenCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), ClientTokenCollection)
            )
        return self.client._get("/client-tokens", operation.get_parameters(), parse)

    def get(self, client_token_id: str) -> ClientToken:
        def parse(response):
            self.response = response
            return ClientToken.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/client-tokens/{client_token_id}", None, parse)

    def create(self, operation: CreateClientToken) -> ClientToken:
        def parse(response):
            self.response = response
            return ClientToken.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/client-tokens", operation, parse)

    def update(self, client_token_id: str, operation: UpdateClientToken) -> ClientToken:
        def parse(response):
            self.response = response
            return ClientToken.from_dict(ResponseParser(response).get_dict())
        return self.client._patch(f"/client-tokens/{client_token_id}", operation, parse)

    def revoke(self, client_token_id: str) -> ClientToken:
        return self.update(client_token_id, UpdateClientToken(status=ClientTokenStatus.Revoked))
