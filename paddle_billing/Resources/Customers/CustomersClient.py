from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import (
    Paginator,
    CreditBalanceCollection,
    CustomerCollection,
    PaymentMethodCollection,
)
from paddle_billing.Entities.Customer import Customer
from paddle_billing.Entities.CustomerAuthToken import CustomerAuthToken
from paddle_billing.Entities.Shared import Status
from paddle_billing.Entities.PaymentMethod import PaymentMethod

from paddle_billing.Resources.Customers.Operations import (
    CreateCustomer,
    ListCreditBalances,
    ListCustomers,
    ListPaymentMethods,
    UpdateCustomer,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class CustomersClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListCustomers = None) -> CustomerCollection:
        if operation is None:
            operation = ListCustomers()

        self.response = self.client.get_raw("/customers", operation.get_parameters())
        parser = ResponseParser(self.response)

        return CustomerCollection.from_list(
            parser.get_data(), Paginator(self.client, parser.get_pagination(), CustomerCollection)
        )

    def get(self, customer_id: str) -> Customer:
        self.response = self.client.get_raw(f"/customers/{customer_id}")
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_data())

    def create(self, operation: CreateCustomer) -> Customer:
        self.response = self.client.post_raw("/customers", operation)
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_data())

    def update(self, customer_id: str, operation: UpdateCustomer) -> Customer:
        self.response = self.client.patch_raw(f"/customers/{customer_id}", operation)
        parser = ResponseParser(self.response)

        return Customer.from_dict(parser.get_data())

    def archive(self, customer_id: str) -> Customer:
        return self.update(customer_id, UpdateCustomer(status=Status.Archived))

    def credit_balances(self, customer_id: str, operation: ListCreditBalances = None) -> CreditBalanceCollection:
        if operation is None:
            operation = ListCreditBalances()

        self.response = self.client.get_raw(f"/customers/{customer_id}/credit-balances", operation)
        parser = ResponseParser(self.response)

        return CreditBalanceCollection.from_list(parser.get_data())

    def create_auth_token(self, customer_id: str) -> CustomerAuthToken:
        self.response = self.client.post_raw(f"/customers/{customer_id}/auth-token")
        parser = ResponseParser(self.response)

        return CustomerAuthToken.from_dict(parser.get_data())

    def list_payment_methods(self, customer_id: str, operation: ListPaymentMethods = None) -> PaymentMethodCollection:
        if operation is None:
            operation = ListPaymentMethods()

        self.response = self.client.get_raw(f"/customers/{customer_id}/payment-methods", operation)
        parser = ResponseParser(self.response)

        return PaymentMethodCollection.from_list(parser.get_data())

    def get_payment_method(self, customer_id: str, payment_method_id: str) -> PaymentMethod:
        self.response = self.client.get_raw(f"/customers/{customer_id}/payment-methods/{payment_method_id}")
        parser = ResponseParser(self.response)

        return PaymentMethod.from_dict(parser.get_data())

    def delete_payment_method(self, customer_id: str, payment_method_id: str) -> None:
        self.response = self.client.delete_raw(f"/customers/{customer_id}/payment-methods/{payment_method_id}")

        return None
