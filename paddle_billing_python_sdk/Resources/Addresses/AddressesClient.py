from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Address                       import Address
from paddle_billing_python_sdk.Entities.Collections.Paginator         import Paginator
from paddle_billing_python_sdk.Entities.Collections.AddressCollection import AddressCollection
from paddle_billing_python_sdk.Entities.Shared.Status                 import Status

from paddle_billing_python_sdk.Resources.Addresses.Operations.CreateAddress import CreateAddress
from paddle_billing_python_sdk.Resources.Addresses.Operations.ListAddresses import ListAddresses
from paddle_billing_python_sdk.Resources.Addresses.Operations.UpdateAddress import UpdateAddress


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class AddressesClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListAddresses = None) -> AddressCollection:
        if operation is None:
            operation = ListAddresses()

        self.response = self.client.get_raw('/addresses', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return AddressCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), AddressCollection)
        )


    def get(self, customer_id: str, address_id: str) -> Address:
        response = self.client.get_raw(f"/customers/{customer_id}/addresses/{address_id}")
        parser   = ResponseParser(response)

        return Address.from_dict(parser.get_data())


    def create(self, customer_id: str, operation: CreateAddress) -> Address:
        self.response = self.client.post_raw(f"/customers/{customer_id}/addresses", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Address.from_dict(parser.get_data())


    def update(self, customer_id: str, address_id: str, operation: UpdateAddress) -> Address:
        self.response = self.client.patch_raw(
            f"/customers/{customer_id}/addresses/{address_id}",
            operation.get_parameters()
        )
        parser = ResponseParser(self.response)

        return Address.from_dict(parser.get_data())


    def archive(self, customer_id: str, address_id: str) -> Address:
        return self.update(customer_id, address_id, UpdateAddress(status=Status.Archived))
