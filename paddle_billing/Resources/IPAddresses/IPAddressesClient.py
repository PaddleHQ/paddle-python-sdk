from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.IPAddresses import IPAddresses

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class IPAddressesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def get_ip_addresses(self) -> IPAddresses:
        def parse(response):
            self.response = response
            return IPAddresses.from_dict(ResponseParser(response).get_dict())
        return self.client._get("/ips", None, parse)
