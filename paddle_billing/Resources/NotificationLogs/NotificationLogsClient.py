from paddle_billing.ResponseParser                        import ResponseParser
from paddle_billing.Entities.Collections                  import Paginator, NotificationLogCollection
from paddle_billing.Resources.NotificationLogs.Operations import ListNotificationLogs

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client import Client


class NotificationLogsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, notification_id: str, operation: ListNotificationLogs = None) -> NotificationLogCollection:
        if operation is None:
            operation = ListNotificationLogs()

        self.response = self.client.get_raw(f"/notifications/{notification_id}/logs", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return NotificationLogCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), NotificationLogCollection)
        )
