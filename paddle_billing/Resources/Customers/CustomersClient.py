from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import (
    Paginator,
    CreditBalanceCollection,
    CustomerCollection,
)
from paddle_billing.Entities.Customer import Customer
from paddle_billing.Entities.CustomerAuthToken import CustomerAuthToken
from paddle_billing.Entities.Shared import Status

from paddle_billing.Resources.Customers.Operations import (
    CreateCustomer,
    ListCreditBalances,
    ListCustomers,
    UpdateCustomer,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class CustomersClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListCustomers | None = None) -> CustomerCollection:
        if operation is None:
            operation = ListCustomers()

        self.response = self.client.get_raw("/customers", operation.get_parameters())
        parser = ResponseParser(self.response)

        return CustomerCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), CustomerCollection)
        )

    def get(self, customer_id: str) -> Customer:
        self.response = self.client.get_raw(f"/customers/{customer_id}")
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_dict())

    def create(self, operation: CreateCustomer) -> Customer:
        self.response = self.client.post_raw("/customers", operation)
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_dict())

    def update(self, customer_id: str, operation: UpdateCustomer) -> Customer:
        self.response = self.client.patch_raw(f"/customers/{customer_id}", operation)
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_dict())

    def archive(self, customer_id: str) -> Customer:
        return self.update(customer_id, UpdateCustomer(status=Status.Archived))

    def credit_balances(self, customer_id: str, operation: ListCreditBalances | None = None) -> CreditBalanceCollection:
        if operation is None:
            operation = ListCreditBalances()

        self.response = self.client.get_raw(f"/customers/{customer_id}/credit-balances", operation)
        parser = ResponseParser(self.response)

        return CreditBalanceCollection.from_list(parser.get_list())

    def create_auth_token(self, customer_id: str) -> CustomerAuthToken:
        self.response = self.client.post_raw(f"/customers/{customer_id}/auth-token")
        parser = ResponseParser(self.response)

        return CustomerAuthToken.from_dict(parser.get_dict())
