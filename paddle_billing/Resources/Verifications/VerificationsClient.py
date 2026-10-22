from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import VerificationCollection, Paginator
from paddle_billing.Entities.Verification import Verification

from paddle_billing.Resources.Verifications.Operations import ListVerifications

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class VerificationsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListVerifications | None = None) -> VerificationCollection:
        if operation is None:
            operation = ListVerifications()

        self.response = self.client.get_raw("/verifications", operation.get_parameters())
        parser = ResponseParser(self.response)

        return VerificationCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), VerificationCollection)
        )

    def get(self, verification_id: str) -> Verification:
        self.response = self.client.get_raw(f"/verifications/{verification_id}")
        parser = ResponseParser(self.response)

        return Verification.from_dict(parser.get_dict())
