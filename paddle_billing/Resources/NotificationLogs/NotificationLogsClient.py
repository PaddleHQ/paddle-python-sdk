from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import NotificationLogCollection
from paddle_billing.Resources.NotificationLogs.Operations import ListNotificationLogs

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class NotificationLogsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, notification_id: str, operation: ListNotificationLogs | None = None) -> NotificationLogCollection:
        if operation is None:
            operation = ListNotificationLogs()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return NotificationLogCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), NotificationLogCollection)
            )
        return self.client._get(f"/notifications/{notification_id}/logs", operation.get_parameters(), parse)
