from requests import Response

from paddle_billing.ResponseParser import ResponseParser as ResponseParser

from paddle_billing.Entities.AccountDetails import AccountDetails as AccountDetails

from paddle_billing.Resources.Account.Operations import UpdateAccount as UpdateAccount

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class AccountClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response: Response | None = None

    def get(self) -> AccountDetails:
        self.response = self.client.get_raw("/account")
        parser = ResponseParser(self.response)

        return AccountDetails.from_dict(parser.get_dict())

    def update(self, operation: UpdateAccount) -> AccountDetails:
        self.response = self.client.patch_raw("/account", operation)
        parser = ResponseParser(self.response)

        return AccountDetails.from_dict(parser.get_dict())
