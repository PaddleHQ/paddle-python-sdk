from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections         import NotificationSettingCollection
from paddle_billing.Entities.NotificationSetting import NotificationSetting

from paddle_billing.Resources.NotificationSettings.Operations import CreateNotificationSetting, UpdateNotificationSetting

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client import Client


class NotificationSettingsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self) -> NotificationSettingCollection:
        self.response = self.client.get_raw('/notification-settings')
        parser        = ResponseParser(self.response)

        return NotificationSettingCollection.from_list(parser.get_data())


    def get(self, notification_setting_id: str) -> NotificationSetting:
        self.response = self.client.get_raw(f"/notification-settings/{notification_setting_id}")
        parser        = ResponseParser(self.response)

        return NotificationSetting.from_dict(parser.get_data())


    def create(self, operation: CreateNotificationSetting) -> NotificationSetting:
        self.response = self.client.post_raw('/notification-settings', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return NotificationSetting.from_dict(parser.get_data())


    def update(self, notification_setting_id: str, operation: UpdateNotificationSetting) -> NotificationSetting:
        self.response = self.client.patch_raw(
            f"/notification-settings/{notification_setting_id}",
            operation.get_parameters()
        )
        parser = ResponseParser(self.response)

        return NotificationSetting.from_dict(parser.get_data())


    def delete(self, notification_setting_id: str) -> NotificationSetting:
        self.response = self.client.delete_raw(f"/notification-settings/{notification_setting_id}")
        parser        = ResponseParser(self.response)

        return NotificationSetting.from_dict(parser.get_data())
