from requests import Response

from paddle_billing.ResponseParser import ResponseParser as ResponseParser

from paddle_billing.Entities.Collections import NotificationCollection as NotificationCollection, Paginator as Paginator
from paddle_billing.Entities.Notification import Notification as Notification

from paddle_billing.Resources.Notifications.Operations import ListNotifications as ListNotifications

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class NotificationsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response: Response | None = None

    def list(self, operation: ListNotifications | None = None) -> NotificationCollection:
        if operation is None:
            operation = ListNotifications()

        self.response = self.client.get_raw("/notifications", operation.get_parameters())
        parser = ResponseParser(self.response)

        return NotificationCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), NotificationCollection)
        )

    def get(self, notification_id: str) -> Notification:
        self.response = self.client.get_raw(f"/notifications/{notification_id}")
        parser = ResponseParser(self.response)

        return Notification.from_dict(parser.get_dict())

    def replay(self, notification_id: str) -> str:
        self.response = self.client.post_raw(f"/notifications/{notification_id}/replay")
        parser = ResponseParser(self.response)
        data = parser.get_dict()

        return data.get("notification_id", "")
