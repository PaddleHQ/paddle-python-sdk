from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Address     import Address
from paddle_billing.Entities.Collections import Paginator, AddressCollection
from paddle_billing.Entities.Shared      import Status

from paddle_billing.Resources.Addresses.Operations import CreateAddress, ListAddresses, UpdateAddress

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client import Client


class AddressesClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, customer_id: str, operation: ListAddresses = None) -> AddressCollection:
        if operation is None:
            operation = ListAddresses()

        self.response = self.client.get_raw(f"/customers/{customer_id}/addresses", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return AddressCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), AddressCollection)
        )


    def get(self, customer_id: str, address_id: str) -> Address:
        self.response = self.client.get_raw(f"/customers/{customer_id}/addresses/{address_id}")
        parser        = ResponseParser(self.response)

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
