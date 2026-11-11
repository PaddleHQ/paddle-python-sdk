from paddle_billing.HasParameters import HasParameters
from paddle_billing.Resources.Shared.Operations import Pager


class ListApiKeyRotations(HasParameters):
    def __init__(self, pager: Pager | None = None):
        self.pager = pager

    def get_parameters(self) -> dict[str, str]:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())

        return parameters
