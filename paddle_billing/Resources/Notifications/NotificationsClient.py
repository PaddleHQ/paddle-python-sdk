from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import NotificationCollection
from paddle_billing.Entities.Notification import Notification

from paddle_billing.Resources.Notifications.Operations import ListNotifications

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class NotificationsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListNotifications | None = None) -> NotificationCollection:
        if operation is None:
            operation = ListNotifications()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return NotificationCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), NotificationCollection)
            )
        return self.client._get("/notifications", operation.get_parameters(), parse)

    def get(self, notification_id: str) -> Notification:
        def parse(response):
            self.response = response
            return Notification.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/notifications/{notification_id}", None, parse)

    def replay(self, notification_id: str) -> str:
        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            data = parser.get_data()
            return data.get("notification_id", "")
        return self.client._post(f"/notifications/{notification_id}/replay", None, parse)
