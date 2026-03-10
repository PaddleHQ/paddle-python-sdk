# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Customers/CustomersClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import (
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
    from paddle_billing.AsyncClient import AsyncClient


class AsyncCustomersClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListCustomers | None = None) -> CustomerCollection:
        if operation is None:
            operation = ListCustomers()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return CustomerCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), CustomerCollection)
            )
        return await self.client._get("/customers", operation.get_parameters(), parse)

    async def get(self, customer_id: str) -> Customer:
        def parse(response):
            self.response = response
            return Customer.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/customers/{customer_id}", None, parse)

    async def create(self, operation: CreateCustomer) -> Customer:
        def parse(response):
            self.response = response
            return Customer.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/customers", operation, parse)

    async def update(self, customer_id: str, operation: UpdateCustomer) -> Customer:
        def parse(response):
            self.response = response
            return Customer.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/customers/{customer_id}", operation, parse)

    async def archive(self, customer_id: str) -> Customer:
        return await self.update(customer_id, UpdateCustomer(status=Status.Archived))

    async def credit_balances(self, customer_id: str, operation: ListCreditBalances | None = None) -> CreditBalanceCollection:
        if operation is None:
            operation = ListCreditBalances()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return CreditBalanceCollection.from_list(parser.get_list())
        return await self.client._get(f"/customers/{customer_id}/credit-balances", operation, parse)

    async def create_auth_token(self, customer_id: str) -> CustomerAuthToken:
        def parse(response):
            self.response = response
            return CustomerAuthToken.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/customers/{customer_id}/auth-token", None, parse)
