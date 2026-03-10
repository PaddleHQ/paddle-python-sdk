from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, PaymentMethodCollection
from paddle_billing.Entities.PaymentMethod import PaymentMethod

from paddle_billing.Resources.PaymentMethods.Operations import ListPaymentMethods

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncPaymentMethodsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, customer_id: str, operation: ListPaymentMethods | None = None) -> PaymentMethodCollection:
        if operation is None:
            operation = ListPaymentMethods()

        self.response = await self.client.get_raw(f"/customers/{customer_id}/payment-methods", operation)
        parser = ResponseParser(self.response)

        return PaymentMethodCollection.from_list(
            parser.get_list(),
            AsyncPaginator(self.client, parser.get_pagination(), PaymentMethodCollection),
        )

    async def get(self, customer_id: str, payment_method_id: str) -> PaymentMethod:
        self.response = await self.client.get_raw(f"/customers/{customer_id}/payment-methods/{payment_method_id}")
        parser = ResponseParser(self.response)

        return PaymentMethod.from_dict(parser.get_dict())

    async def delete(self, customer_id: str, payment_method_id: str) -> None:
        self.response = await self.client.delete_raw(f"/customers/{customer_id}/payment-methods/{payment_method_id}")

        return None
