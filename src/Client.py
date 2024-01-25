import requests
from requests.adapters  import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin, urlencode
from uuid               import uuid4

from json import dumps as json_dumps
from urllib.parse import urlparse


# from src.Logger.Formatter                                          import CustomLogger
# from src.Entities.Addresses.AddressesClient                        import AddressesClient
# from src.Entities.Adjustment.AdjustmentsClient                     import AdjustmentsClient
# from src.Entities.Businesses.BusinessesClient                      import BusinessesClient
# from src.Entities.Customers.CustomersClient                        import CustomersClient
# from src.Entities.Discounts.DiscountsClient                        import DiscountsClient
# from src.Entities.Events.EventsClient                              import EventsClient
# from src.Entities.EventTypes.EventTypesClient                      import EventTypesClient
# from src.Entities.NotificationLogs.NotificationLogsClient          import NotificationLogsClient
# from src.Entities.Notifications.NotificationsClient                import NotificationsClient
# from src.Entities.NotificationSettings.NotificationSettingsClient  import NotificationSettingsClient
# from src.Entities.Prices.PricesClient                              import PricesClient
# from src.Entities.PricingPreviews.PricingPreviewsClient            import PricingPreviewsClient
# from src.Entities.Products.ProductsClient                          import ProductsClient
# from src.Entities.Reports.ReportsClient                            import ReportsClient
# from src.Entities.Subscriptions.SubscriptionsClient                import SubscriptionsClient
# from src.Entities.Transactions.TransactionsClient                  import TransactionsClient


class Client:
    """
    Client for making API requests using Python's requests library.
    """

    SDK_VERSION = '0.0.1a20'


    def __init__(
        self,
        api_key:     str,             # handle our api key class
        options:     dict     = None,
        http_client: requests = None,
        logger                = None,
        retry_count: int      = 3,
    ):
        self.api_key        = api_key
        self.options        = options if options else {}
        self.logger         = logger
        self.retry_count    = retry_count
        self.transaction_id = None
        self.client         = self.build_request_session()

        # Initialize other clients as needed
        # self.products = ProductsClient(self)
        # ... Initialize other resource clients here ...


    def logging_hook(self, response, *args, **kwargs):
        self.logger.info(f"Request:  {response.request.method} {response.request.url}")
        self.logger.info(f"Response: {response.status_code} {response.text}")


    def _make_request(
        self,
        method:     str,
        uri:        str,
        payload:    dict | None = None,
    ):
        # Parse and update URI with base URL components if necessary
        if isinstance(uri, str):
            uri = urljoin(self.options['environment'].base_url, uri)

        self.client.headers.update({
            'X-Transaction-ID': str(self.transaction_id) if self.transaction_id else str(uuid4())
        })

        # Serialize payload to JSON
        final_json = None
        if payload is not None:
            json_payload = json_dumps(payload)
            final_json   = json_payload if json_payload == '[]' else '{}'

        # We're only ever passing JSON data, should be pretty safe to use json= instead of body=
        try:
            response = self.client.request(method.upper(), uri, json=final_json)
            response.raise_for_status()

            return response
        except requests.RequestException as e:
            if self.logger:
                self.logger.error(f"Request failed: {e}")
            raise


    def get_raw(self, uri, parameters=None):
        return self._make_request('GET', uri, None, parameters)


    def post_raw(self, uri, payload=None, parameters=None):
        return self._make_request('POST', uri, payload, parameters)


    def patch_raw(self, uri, payload):
        return self._make_request('PATCH', uri, payload)


    def delete_raw(self, uri):
        return self._make_request('DELETE', uri)


    def build_request_session(self):
        session = requests.Session()
        session.headers.update({
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type':  'application/json',
            'User-Agent':    f"paddle-billing-python-sdk {self.SDK_VERSION}",
        })

        # Configure retries
        retries = Retry(total=self.retry_count, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session.mount('https://', HTTPAdapter(max_retries=retries))

        # Handle logging
        if self.logger:
            session.hooks['response'] = self.logging_hook

        return session


# Example usage
# client = Client(api_key="your_api_key", logger=your_logger_instance)
# response = client.make_request('GET', 'https://api.example.com/data')
