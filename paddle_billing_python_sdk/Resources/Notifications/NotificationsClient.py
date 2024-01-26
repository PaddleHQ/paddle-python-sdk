from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Notification                       import Notification
from paddle_billing_python_sdk.Entities.Collections.NotificationCollection import NotificationCollection
from paddle_billing_python_sdk.Entities.Collections.Paginator              import Paginator

from paddle_billing_python_sdk.Resources.Notifications.Operations.ListNotifications import ListNotifications


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class NotificationsClient:
    def __init__(self, client: 'Client'):
        self.client = client


    def list(self, operation: ListNotifications = None) -> NotificationCollection:
        if operation is None:
            operation = ListNotifications()

        response = self.client.get_raw('/notifications', operation.get_parameters())
        parser   = ResponseParser(response)

        return NotificationCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), NotificationCollection)
        )


    def get(self, notification_setting_id: str) -> Notification:
        response = self.client.get_raw(f"/notifications/{notification_setting_id}")
        parser   = ResponseParser(response)

        return Notification.from_dict(parser.get_data())


    def replay(self, notification_setting_id: str) -> str:
        response = self.client.post_raw(f"/notifications/{notification_setting_id}")
        parser   = ResponseParser(response)
        data     = parser.get_data()

        return data.get('notification_id', '')
