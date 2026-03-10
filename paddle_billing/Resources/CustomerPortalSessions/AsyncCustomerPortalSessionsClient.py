# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/CustomerPortalSessions/CustomerPortalSessionsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.CustomerPortalSession import CustomerPortalSession

from paddle_billing.Resources.CustomerPortalSessions.Operations import (
    CreateCustomerPortalSession,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncCustomerPortalSessionsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def create(self, customer_id: str, operation: CreateCustomerPortalSession) -> CustomerPortalSession:
        def parse(response):
            self.response = response
            return CustomerPortalSession.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/customers/{customer_id}/portal-sessions", operation, parse)
