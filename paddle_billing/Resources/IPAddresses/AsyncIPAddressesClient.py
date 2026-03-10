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
        self.response = await self.client.get_raw("/ips")
        parser = ResponseParser(self.response)

        return IPAddresses.from_dict(parser.get_dict())
