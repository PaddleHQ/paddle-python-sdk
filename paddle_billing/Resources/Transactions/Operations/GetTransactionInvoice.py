from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import Disposition


class GetTransactionInvoice(HasParameters):
    def __init__(
        self,
        disposition: Disposition | None = None,
    ):
        self.disposition = disposition

    def get_parameters(self) -> dict[str, str]:
        parameters = {}

        if self.disposition:
            parameters["disposition"] = self.disposition.value

        return parameters
