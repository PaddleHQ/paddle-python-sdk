from typing import TYPE_CHECKING

from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Customer                            import Customer
from paddle_billing.Entities.Collections.Paginator               import Paginator
from paddle_billing.Entities.Collections.CreditBalanceCollection import CreditBalanceCollection
from paddle_billing.Entities.Collections.CustomerCollection      import CustomerCollection
from paddle_billing.Entities.Shared.Status                       import Status

from paddle_billing.Resources.Customers.Operations.CreateCustomer import CreateCustomer
from paddle_billing.Resources.Customers.Operations.ListCustomers  import ListCustomers
from paddle_billing.Resources.Customers.Operations.UpdateCustomer import UpdateCustomer


if TYPE_CHECKING:
    from paddle_billing.Client import Client


class CustomersClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListCustomers = None) -> CustomerCollection:
        if operation is None:
            operation = ListCustomers()

        self.response = self.client.get_raw('/customers', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return CustomerCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), CustomerCollection)
        )


    def get(self, customer_id: str) -> Customer:
        self.response = self.client.get_raw(f"/customers/{customer_id}")
        parser        = ResponseParser(self.response)

        return Customer.from_dict(parser.get_data())


    def create(self, operation: CreateCustomer) -> Customer:
        self.response = self.client.post_raw('/customers', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Customer.from_dict(parser.get_data())


    def update(self, customer_id: str, operation: UpdateCustomer) -> Customer:
        self.response = self.client.patch_raw(f"/customers/{customer_id}", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Customer.from_dict(parser.get_data())


    def archive(self, customer_id: str) -> Customer:
        return self.update(customer_id, UpdateCustomer(status=Status.Archived))


    def credit_balances(self, customer_id: str) -> CreditBalanceCollection:
        self.response = self.client.get_raw(f"/customers/{customer_id}/credit-balances")
        parser        = ResponseParser(self.response)

        return CreditBalanceCollection.from_list(parser.get_data())
