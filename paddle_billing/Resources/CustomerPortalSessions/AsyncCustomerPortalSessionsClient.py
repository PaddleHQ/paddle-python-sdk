from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.CustomerPortalSession import CustomerPortalSession

from paddle_billing.Resources.CustomerPortalSessions.Operations import CreateCustomerPortalSession

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncCustomerPortalSessionsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def create(self, customer_id: str, operation: CreateCustomerPortalSession) -> CustomerPortalSession:
        self.response = await self.client.post_raw(f"/customers/{customer_id}/portal-sessions", operation)
        parser = ResponseParser(self.response)

        return CustomerPortalSession.from_dict(parser.get_dict())
