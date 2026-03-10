from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import (
    PaymentMethodCollection,
)
from paddle_billing.Entities.PaymentMethod import PaymentMethod

from paddle_billing.Resources.PaymentMethods.Operations import (
    ListPaymentMethods,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class PaymentMethodsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, customer_id: str, operation: ListPaymentMethods | None = None) -> PaymentMethodCollection:
        if operation is None:
            operation = ListPaymentMethods()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return PaymentMethodCollection.from_list(
                parser.get_list(),
                self.client._make_paginator(parser.get_pagination(), PaymentMethodCollection),
            )
        return self.client._get(f"/customers/{customer_id}/payment-methods", operation, parse)

    def get(self, customer_id: str, payment_method_id: str) -> PaymentMethod:
        def parse(response):
            self.response = response
            return PaymentMethod.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/customers/{customer_id}/payment-methods/{payment_method_id}", None, parse)

    def delete(self, customer_id: str, payment_method_id: str) -> None:
        self.client._delete(f"/customers/{customer_id}/payment-methods/{payment_method_id}")

        return None
