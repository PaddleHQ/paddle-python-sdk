from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections          import NotificationSettingCollection
from paddle_billing.Entities.Events               import EventTypeName
from paddle_billing.Entities.NotificationSetting  import NotificationSetting
from paddle_billing.Entities.NotificationSettings import NotificationSettingType

from paddle_billing.Resources.NotificationSettings.Operations import CreateNotificationSetting, UpdateNotificationSetting

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestNotificationSettingsClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                CreateNotificationSetting(
                    description              = 'Slack notifications',
                    type                     = NotificationSettingType.Url,
                    destination              = 'https://hooks.slack.com/example',
                    include_sensitive_fields = False,
                    subscribed_events        = [
                        EventTypeName.TransactionBilled,
                        EventTypeName.TransactionCanceled,
                        EventTypeName.TransactionCompleted,
                        EventTypeName.TransactionCreated,
                        EventTypeName.TransactionPaymentFailed,
                        EventTypeName.SubscriptionCreated,
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/notification-settings',
            ), (
                CreateNotificationSetting(
                    api_version              = 1,
                    description              = 'Slack notifications',
                    type                     = NotificationSettingType.Url,
                    destination              = 'https://hooks.slack.com/example',
                    include_sensitive_fields = False,
                    subscribed_events        = [
                        EventTypeName.TransactionBilled,
                        EventTypeName.TransactionCanceled,
                        EventTypeName.TransactionCompleted,
                        EventTypeName.TransactionCreated,
                        EventTypeName.TransactionPaymentFailed,
                        EventTypeName.TransactionReady,
                        EventTypeName.TransactionUpdated,
                        EventTypeName.SubscriptionActivated,
                        EventTypeName.SubscriptionCreated,
                        EventTypeName.SubscriptionPastDue,
                        EventTypeName.SubscriptionPaused,
                        EventTypeName.SubscriptionResumed,
                        EventTypeName.SubscriptionTrialing,
                        EventTypeName.SubscriptionUpdated,
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/notification-settings',
            ),
        ],
        ids=[
            "Create notification-setting with basic data",
            "Create notification-setting with full data",
        ],
    )
    def test_create_notification_setting_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.notification_settings.create(operation)
        response_json = test_client.client.notification_settings.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, NotificationSetting)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'notification_setting_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
                UpdateNotificationSetting(active=False),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/notification-settings/ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
            ), (
                'ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
                UpdateNotificationSetting(description='Slack notifications (old)', active=False),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/notification-settings/ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
            ), (
                'ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
                UpdateNotificationSetting(
                    active                   = False,
                    api_version              = 1,
                    description              = 'Slack notifications (old)',
                    destination              = 'https://hooks.slack.com/example',
                    include_sensitive_fields = False,
                    subscribed_events        = [
                        EventTypeName.TransactionBilled,
                        EventTypeName.TransactionCanceled,
                        EventTypeName.TransactionCompleted,
                        EventTypeName.TransactionCreated,
                        EventTypeName.TransactionPaymentFailed,
                        EventTypeName.TransactionReady,
                        EventTypeName.TransactionUpdated,
                        EventTypeName.SubscriptionActivated,
                        EventTypeName.SubscriptionCreated,
                        EventTypeName.SubscriptionPastDue,
                        EventTypeName.SubscriptionPaused,
                        EventTypeName.SubscriptionResumed,
                        EventTypeName.SubscriptionTrialing,
                        EventTypeName.SubscriptionUpdated,
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/notification-settings/ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
            ),
        ],
        ids=[
            "Update notification setting with basic data",
            "Update notification setting with partial data",
            "Update notification setting with full data",
        ],
    )
    def test_update_notification_setting_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        notification_setting_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.notification_settings.update(notification_setting_id, operation)
        response_json = test_client.client.notification_settings.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, NotificationSetting)
        assert last_request is not None
        assert last_request.method            == 'PATCH'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'expected_response_status, expected_response_body, expected_url',
        [(200, ReadsFixtures.read_raw_json_fixture('response/list_default'), '/notification-settings',)],
        ids=["List notification-settings"],
    )
    def test_list_notification_settings_returns_expected_response(
        self,
        test_client,
        mock_requests,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status)

        response     = test_client.client.notification_settings.list()
        last_request = mock_requests.last_request

        assert isinstance(response, NotificationSettingCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'notification_setting_id, expected_response_status, expected_response_body, expected_url',
        [(
                'ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/notification-settings/ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
        )],
        ids=["Get a notification setting by its id"],
    )
    def test_get_notification_settings_returns_expected_response(
        self,
        test_client,
        mock_requests,
        notification_setting_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.notification_settings.get(notification_setting_id)
        response_json = test_client.client.notification_settings.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, NotificationSetting)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"


    @mark.parametrize(
        'notification_setting_id, expected_response_status, expected_response_body, expected_url',
        [(
                'ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/notification-settings/ntfset_01gkpjp8bkm3tm53kdgkx6sms7',
        )],
        ids=["Delete a notification setting by its id"],
    )
    def test_delete_notification_setting_returns_expected_response(
        self,
        test_client,
        mock_requests,
        notification_setting_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        """Although the API doesn't specify a returned body, in practice it returns the deleted notification setting."""

        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.delete(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.notification_settings.delete(notification_setting_id)
        response_json = test_client.client.notification_settings.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, NotificationSetting)
        assert last_request is not None
        assert last_request.method            == 'DELETE'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
