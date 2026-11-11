from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import Paginator, ApiKeyCollection, ApiKeyRotationCollection
from paddle_billing.Entities.ApiKey import ApiKey
from paddle_billing.Entities.ApiKeyRotation import ApiKeyRotation
from paddle_billing.Entities.ApiKeyRotationCreated import ApiKeyRotationCreated

from paddle_billing.Resources.ApiKeys.Operations import CreateApiKeyRotation, ListApiKeyRotations, ListApiKeys

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class ApiKeysClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListApiKeys | None = None) -> ApiKeyCollection:
        if operation is None:
            operation = ListApiKeys()

        self.response = self.client.get_raw("/api-keys", operation.get_parameters())
        parser = ResponseParser(self.response)

        return ApiKeyCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), ApiKeyCollection)
        )

    def get(self, api_key_id: str) -> ApiKey:
        self.response = self.client.get_raw(f"/api-keys/{api_key_id}")
        parser = ResponseParser(self.response)

        return ApiKey.from_dict(parser.get_dict())

    def list_rotations(self, api_key_id: str, operation: ListApiKeyRotations | None = None) -> ApiKeyRotationCollection:
        if operation is None:
            operation = ListApiKeyRotations()

        self.response = self.client.get_raw(f"/api-keys/{api_key_id}/rotations", operation.get_parameters())
        parser = ResponseParser(self.response)

        return ApiKeyRotationCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), ApiKeyRotationCollection)
        )

    def get_rotation(self, api_key_id: str, rotation_id: str) -> ApiKeyRotation:
        self.response = self.client.get_raw(f"/api-keys/{api_key_id}/rotations/{rotation_id}")
        parser = ResponseParser(self.response)

        return ApiKeyRotation.from_dict(parser.get_dict())

    def create_rotation(self, api_key_id: str, operation: CreateApiKeyRotation) -> ApiKeyRotationCreated:
        self.response = self.client.post_raw(f"/api-keys/{api_key_id}/rotations", operation)
        parser = ResponseParser(self.response)

        return ApiKeyRotationCreated.from_dict(parser.get_dict())
