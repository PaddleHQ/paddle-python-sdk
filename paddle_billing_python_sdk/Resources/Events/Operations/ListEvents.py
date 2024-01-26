from paddle_billing_python_sdk.HasParameters import HasParameters

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager


class ListEvents(HasParameters):
    def __init__(self, pager: Pager = None):
        self.pager = pager


    def get_parameters(self) -> dict:
        return self.pager.get_parameters() if self.pager else {}
