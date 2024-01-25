from logging            import getLogger
from json               import dumps as json_dumps
from requests           import request, RequestException, Session
from requests.adapters  import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse       import urljoin, urlencode
from uuid               import uuid4

from src.HasParameters import HasParameters
from src.Options       import Options

# from src.Logger.Formatter                                          import CustomLogger
from src.Logger.NullHandler                                        import NullHandler

# from src.Resources.Addresses.AddressesClient                        import AddressesClient
# from src.Resources.Adjustment.AdjustmentsClient                     import AdjustmentsClient
# from src.Resources.Businesses.BusinessesClient                      import BusinessesClient
# from src.Resources.Customers.CustomersClient                        import CustomersClient
# from src.Resources.Discounts.DiscountsClient                        import DiscountsClient
# from src.Resources.Events.EventsClient                              import EventsClient
# from src.Resources.EventTypes.EventTypesClient                      import EventTypesClient
# from src.Resources.NotificationLogs.NotificationLogsClient          import NotificationLogsClient
# from src.Resources.Notifications.NotificationsClient                import NotificationsClient
# from src.Resources.NotificationSettings.NotificationSettingsClient  import NotificationSettingsClient
from src.Resources.Prices.PricesClient                              import PricesClient
# from src.Resources.PricingPreviews.PricingPreviewsClient            import PricingPreviewsClient
# from src.Resources.Products.ProductsClient                          import ProductsClient
# from src.Resources.Reports.ReportsClient                            import ReportsClient
# from src.Resources.Subscriptions.SubscriptionsClient                import SubscriptionsClient
# from src.Resources.Transactions.TransactionsClient                  import TransactionsClient


class Client:
    """
    Client for making API requests using Python's requests library.
    """

    SDK_VERSION = '0.0.1a21'


    def __init__(
        self,
        api_key:     str,             # handle our api key class
        options:     dict     = None,
        http_client: Session  = None,
        logger                = None,
        retry_count: int      = 3,
    ):
        self.__api_key      = api_key
        self.options        = options if options else Options()
        self.logger         = logger  if logger  else Client.null_logger()
        self.retry_count    = retry_count
        self.transaction_id = None
        self.client         = self.build_request_session() if not http_client else http_client

        # TODO
        # Initialize other clients as needed
        # self.products = ProductsClient(self)
        self.prices = PricesClient(self)
        # ... Initialize other resource clients here ...


    @staticmethod
    def null_logger():
        """
        Create a logger instance that logs everything to nowhere
        """

        null_logger = getLogger('null_logger')
        null_logger.addHandler(NullHandler())

        return null_logger


    def logging_hook(self, response, *args, **kwargs):
        """
        Requests logs were redirected here and to our custom logger which filters out sensitive data
        """

        self.logger.debug(f"Request:  {response.request.method} {response.request.url}")
        self.logger.debug(f"Response: {response.status_code} {response.text}")


    def _make_request(
        self,
        method:     str,
        uri:        str,
        payload:    dict | None = None,
    ):
        """
        Makes an actual API call to Paddle
        """

        # Parse and update URI with base URL components if necessary
        if isinstance(uri, str):
            uri = urljoin(self.options['environment'].base_url, uri)

        self.client.headers.update({
            'X-Transaction-ID': str(self.transaction_id) if self.transaction_id else str(uuid4())
        })

        # Serialize payload to JSON
        final_json = None
        if payload:
            json_payload = json_dumps(payload)
            final_json   = json_payload if json_payload == '[]' else '{}'

        # We're only ever passing JSON data, should be pretty safe to use json= instead of body=
        try:
            response = self.client.request(method.upper(), uri, json=final_json)
            response.raise_for_status()

            return response
        except RequestException as e:
            if self.logger:
                self.logger.error(f"Request failed: {e}")
            raise


    @staticmethod
    def _format_uri_parameters(uri, parameters: HasParameters):
        if isinstance(parameters, HasParameters):
            parameters = parameters.get_parameters()

            query = urlencode(parameters)
            uri  += '&' if '?' in uri else '?'
            uri  += query

        return uri


    def get_raw(self, uri, parameters=None):
        uri = Client._format_uri_parameters(uri, parameters) if parameters else uri

        return self._make_request('GET', uri, None)


    def post_raw(self, uri, payload=None, parameters=None):
        uri = Client._format_uri_parameters(uri, parameters) if parameters else uri

        return self._make_request('POST', uri, payload)


    def patch_raw(self, uri, payload):
        return self._make_request('PATCH', uri, payload)


    def delete_raw(self, uri):
        return self._make_request('DELETE', uri)


    def build_request_session(self):
        session = Session()
        session.headers.update({
            'Authorization': f"Bearer {self.__api_key}",
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
