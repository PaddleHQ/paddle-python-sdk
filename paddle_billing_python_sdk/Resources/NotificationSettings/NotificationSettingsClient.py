from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.NotificationSetting                       import NotificationSetting
from paddle_billing_python_sdk.Entities.Collections.NotificationSettingCollection import NotificationSettingCollection

from paddle_billing_python_sdk.Resources.NotificationSettings.Operations.CreateNotificationSetting import CreateNotificationSetting
from paddle_billing_python_sdk.Resources.NotificationSettings.Operations.UpdateNotificationSetting import UpdateNotificationSetting


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class NotificationSettingsClient:
    def __init__(self, client: 'Client'):
        self.client = client


    def list(self) -> NotificationSettingCollection:
        response = self.client.get_raw('/notification-settings')
        parser   = ResponseParser(response)

        return NotificationSettingCollection.from_list(parser.get_data())


    def get(self, notification_setting_id: str) -> NotificationSetting:
        response = self.client.get_raw(f"/notification-settings/{notification_setting_id}")
        parser   = ResponseParser(response)

        return NotificationSetting.from_dict(parser.get_data())


    def create(self, operation: CreateNotificationSetting) -> NotificationSetting:
        response = self.client.post_raw('/notification-settings', operation.get_parameters())
        parser   = ResponseParser(response)

        return NotificationSetting.from_dict(parser.get_data())


    def update(self, notification_setting_id: str, operation: UpdateNotificationSetting) -> NotificationSetting:
        response = self.client.patch_raw(
            f"/notification-settings/{notification_setting_id}",
            operation.get_parameters()
        )
        parser = ResponseParser(response)

        return NotificationSetting.from_dict(parser.get_data())


    def delete(self, notification_setting_id: str) -> NotificationSetting:
        response = self.client.delete_raw(f"/notification-settings/{notification_setting_id}")
        parser   = ResponseParser(response)

        return NotificationSetting.from_dict(parser.get_data())
