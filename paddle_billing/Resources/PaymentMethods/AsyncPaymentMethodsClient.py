# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/PaymentMethods/PaymentMethodsClient.py
# Regenerate with: python scripts/generate_async_clients.py
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
    from paddle_billing.AsyncClient import AsyncClient


class AsyncPaymentMethodsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, customer_id: str, operation: ListPaymentMethods | None = None) -> PaymentMethodCollection:
        if operation is None:
            operation = ListPaymentMethods()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return PaymentMethodCollection.from_list(
                parser.get_list(),
                self.client._make_paginator(parser.get_pagination(), PaymentMethodCollection),
            )
        return await self.client._get(f"/customers/{customer_id}/payment-methods", operation, parse)

    async def get(self, customer_id: str, payment_method_id: str) -> PaymentMethod:
        def parse(response):
            self.response = response
            return PaymentMethod.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/customers/{customer_id}/payment-methods/{payment_method_id}", None, parse)

    async def delete(self, customer_id: str, payment_method_id: str) -> None:
        self.client._delete(f"/customers/{customer_id}/payment-methods/{payment_method_id}")

        return None
