from paddle_billing.HasParameters import HasParameters
from paddle_billing.Resources.Shared.Operations import Pager


class ListNotificationLogs(HasParameters):
    def __init__(self, pager: Pager | None = None):
        self.pager = pager

    def get_parameters(self) -> dict[str, str]:
        return self.pager.get_parameters() if self.pager else {}
