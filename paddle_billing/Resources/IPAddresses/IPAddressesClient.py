from requests import Response

from paddle_billing.ResponseParser import ResponseParser as ResponseParser

from paddle_billing.Entities.IPAddresses import IPAddresses as IPAddresses

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class IPAddressesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response: Response | None = None

    def get_ip_addresses(self) -> IPAddresses:
        self.response = self.client.get_raw("/ips")
        parser = ResponseParser(self.response)

        return IPAddresses.from_dict(parser.get_dict())
