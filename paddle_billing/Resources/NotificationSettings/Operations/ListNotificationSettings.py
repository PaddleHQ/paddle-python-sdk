from paddle_billing.HasParameters import HasParameters

from paddle_billing.Resources.Shared.Operations import Pager


class ListNotificationSettings(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        active: bool | None = None,
    ):
        self.pager = pager
        self.active = active

    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.active is not None:
            parameters["active"] = "true" if self.active else "false"

        return parameters
