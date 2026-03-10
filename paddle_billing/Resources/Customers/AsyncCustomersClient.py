from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, CreditBalanceCollection, CustomerCollection
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
    from paddle_billing.AsyncClient import AsyncClient


class AsyncCustomersClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListCustomers | None = None) -> CustomerCollection:
        if operation is None:
            operation = ListCustomers()

        self.response = await self.client.get_raw("/customers", operation.get_parameters())
        parser = ResponseParser(self.response)

        return CustomerCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), CustomerCollection)
        )

    async def get(self, customer_id: str) -> Customer:
        self.response = await self.client.get_raw(f"/customers/{customer_id}")
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_dict())

    async def create(self, operation: CreateCustomer) -> Customer:
        self.response = await self.client.post_raw("/customers", operation)
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_dict())

    async def update(self, customer_id: str, operation: UpdateCustomer) -> Customer:
        self.response = await self.client.patch_raw(f"/customers/{customer_id}", operation)
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_dict())

    async def archive(self, customer_id: str) -> Customer:
        return await self.update(customer_id, UpdateCustomer(status=Status.Archived))

    async def credit_balances(
        self, customer_id: str, operation: ListCreditBalances | None = None
    ) -> CreditBalanceCollection:
        if operation is None:
            operation = ListCreditBalances()

        self.response = await self.client.get_raw(f"/customers/{customer_id}/credit-balances", operation)
        parser = ResponseParser(self.response)

        return CreditBalanceCollection.from_list(parser.get_list())

    async def create_auth_token(self, customer_id: str) -> CustomerAuthToken:
        self.response = await self.client.post_raw(f"/customers/{customer_id}/auth-token")
        parser = ResponseParser(self.response)

        return CustomerAuthToken.from_dict(parser.get_dict())
