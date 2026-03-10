# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/IPAddresses/IPAddressesClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.IPAddresses import IPAddresses

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncIPAddressesClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def get_ip_addresses(self) -> IPAddresses:
        def parse(response):
            self.response = response
            return IPAddresses.from_dict(ResponseParser(response).get_dict())
        return await self.client._get("/ips", None, parse)
