from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.CustomerPortalSession import CustomerPortalSession

from paddle_billing.Resources.CustomerPortalSessions.Operations import (
    CreateCustomerPortalSession,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class CustomerPortalSessionsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def create(self, customer_id: str, operation: CreateCustomerPortalSession) -> CustomerPortalSession:
        def parse(response):
            self.response = response
            return CustomerPortalSession.from_dict(ResponseParser(response).get_dict())
        return self.client._post(f"/customers/{customer_id}/portal-sessions", operation, parse)
