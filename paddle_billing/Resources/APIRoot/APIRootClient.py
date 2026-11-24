from requests import Response

from paddle_billing.ResponseParser import ResponseParser as ResponseParser

from paddle_billing.Entities.RootContext import RootContext as RootContext

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class APIRootClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response: Response | None = None

    def get(self) -> RootContext:
        self.response = self.client.get_raw("/")
        parser = ResponseParser(self.response)

        return RootContext.from_dict(parser.get_dict())
