from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.DateTime      import DateTime
from paddle_billing.Entities.Notifications import NotificationStatus

from paddle_billing.Resources.Shared.Operations import Pager


class ListNotifications(HasParameters):
    def __init__(
        self,
        pager:                   Pager                    | None = None,
        notification_setting_id: list[str]                       = None,
        search:                  str                      | None = None,
        statuses:                list[NotificationStatus]        = None,
        filter:                  str                      | None = None,
        end:                     DateTime                 | None = None,
        start:                   DateTime                 | None = None,
    ):
        self.pager                   = pager
        self.search                  = search
        self.filter                  = filter
        self.end                     = end  # DateTime.from_datetime(end)
        self.start                   = start  # DateTime.from_datetime(start)
        self.notification_setting_id = notification_setting_id if notification_setting_id is not None else []
        self.statuses                = statuses                if statuses                is not None else []


    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.notification_setting_id:
            parameters['notification_setting_id'] = ','.join(self.notification_setting_id)
        if self.search:
            parameters['search'] = self.search
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.filter:
            parameters['filter'] = self.filter
        if self.end:
            parameters['to'] = self.end.format()
        if self.start:
            parameters['from'] = self.start.format()

        return parameters
