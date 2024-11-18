from paddle_billing.HasParameters import HasParameters

from paddle_billing.Resources.Shared.Operations import Pager

from paddle_billing.Entities.NotificationSettings import NotificationSettingTrafficSource


class ListNotificationSettings(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        active: bool | None = None,
        traffic_source: NotificationSettingTrafficSource | None = None,
    ):
        self.pager = pager
        self.active = active
        self.traffic_source = traffic_source

    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.active is not None:
            parameters["active"] = "true" if self.active else "false"
        if self.traffic_source is not None:
            parameters["traffic_source"] = self.traffic_source.value

        return parameters
