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
        self.client   = client
        self.response = None


    def list(self, operation: ListNotifications = None) -> NotificationCollection:
        if operation is None:
            operation = ListNotifications()

        self.response = self.client.get_raw('/notifications', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return NotificationCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), NotificationCollection)
        )


    def get(self, notification_id: str) -> Notification:
        self.response = self.client.get_raw(f"/notifications/{notification_id}")
        parser        = ResponseParser(self.response)

        return Notification.from_dict(parser.get_data())


    def replay(self, notification_id: str) -> str:
        self.response = self.client.post_raw(f"/notifications/{notification_id}")
        parser        = ResponseParser(self.response)
        data          = parser.get_data()

        return data.get('notification_id', '')
