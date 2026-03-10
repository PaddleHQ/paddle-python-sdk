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
    from paddle_billing.Client import Client


class CustomersClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListCustomers | None = None) -> CustomerCollection:
        if operation is None:
            operation = ListCustomers()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return CustomerCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), CustomerCollection)
            )
        return self.client._get("/customers", operation.get_parameters(), parse)

    def get(self, customer_id: str) -> Customer:
        def parse(response):
            self.response = response
            return Customer.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/customers/{customer_id}", None, parse)

    def create(self, operation: CreateCustomer) -> Customer:
        def parse(response):
            self.response = response
            return Customer.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/customers", operation, parse)

    def update(self, customer_id: str, operation: UpdateCustomer) -> Customer:
        def parse(response):
            self.response = response
            return Customer.from_dict(ResponseParser(response).get_dict())
        return self.client._patch(f"/customers/{customer_id}", operation, parse)

    def archive(self, customer_id: str) -> Customer:
        return self.update(customer_id, UpdateCustomer(status=Status.Archived))

    def credit_balances(self, customer_id: str, operation: ListCreditBalances | None = None) -> CreditBalanceCollection:
        if operation is None:
            operation = ListCreditBalances()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return CreditBalanceCollection.from_list(parser.get_list())
        return self.client._get(f"/customers/{customer_id}/credit-balances", operation, parse)

    def create_auth_token(self, customer_id: str) -> CustomerAuthToken:
        def parse(response):
            self.response = response
            return CustomerAuthToken.from_dict(ResponseParser(response).get_dict())
        return self.client._post(f"/customers/{customer_id}/auth-token", None, parse)
