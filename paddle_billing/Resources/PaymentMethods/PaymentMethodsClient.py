from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import (
    PaymentMethodCollection,
    Paginator,
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

        self.response = self.client.get_raw(f"/customers/{customer_id}/payment-methods", operation)
        parser = ResponseParser(self.response)

        return PaymentMethodCollection.from_list(
            parser.get_list(),
            Paginator(self.client, parser.get_pagination(), PaymentMethodCollection),
        )

    def get(self, customer_id: str, payment_method_id: str) -> PaymentMethod:
        self.response = self.client.get_raw(f"/customers/{customer_id}/payment-methods/{payment_method_id}")
        parser = ResponseParser(self.response)

        return PaymentMethod.from_dict(parser.get_dict())

    def delete(self, customer_id: str, payment_method_id: str) -> None:
        self.response = self.client.delete_raw(f"/customers/{customer_id}/payment-methods/{payment_method_id}")

        return None
