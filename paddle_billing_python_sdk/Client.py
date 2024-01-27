from logging            import Logger, getLogger
from json               import dumps as json_dumps
from requests           import Response, RequestException, Session
from requests.adapters  import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse       import urljoin, urlencode
from uuid               import uuid4

from paddle_billing_python_sdk.__VERSION__      import __VERSION__
from paddle_billing_python_sdk.FiltersNone      import FiltersNone
from paddle_billing_python_sdk.FiltersUndefined import FiltersUndefined
from paddle_billing_python_sdk.HasParameters    import HasParameters
from paddle_billing_python_sdk.Options          import Options

# from paddle_billing_python_sdk.Logger.Formatter                                          import CustomLogger
from paddle_billing_python_sdk.Logger.NullHandler                                        import NullHandler

from paddle_billing_python_sdk.Resources.Addresses.AddressesClient                        import AddressesClient
from paddle_billing_python_sdk.Resources.Adjustments.AdjustmentsClient                    import AdjustmentsClient
from paddle_billing_python_sdk.Resources.Businesses.BusinessesClient                      import BusinessesClient
from paddle_billing_python_sdk.Resources.Customers.CustomersClient                        import CustomersClient
from paddle_billing_python_sdk.Resources.Discounts.DiscountsClient                        import DiscountsClient
from paddle_billing_python_sdk.Resources.Events.EventsClient                              import EventsClient
from paddle_billing_python_sdk.Resources.EventTypes.EventTypesClient                      import EventTypesClient
from paddle_billing_python_sdk.Resources.Notifications.NotificationsClient                import NotificationsClient
from paddle_billing_python_sdk.Resources.NotificationLogs.NotificationLogsClient          import NotificationLogsClient
from paddle_billing_python_sdk.Resources.NotificationSettings.NotificationSettingsClient  import NotificationSettingsClient
from paddle_billing_python_sdk.Resources.Prices.PricesClient                              import PricesClient
from paddle_billing_python_sdk.Resources.PricingPreviews.PricingPreviewsClient            import PricingPreviewsClient
from paddle_billing_python_sdk.Resources.Products.ProductsClient                          import ProductsClient
from paddle_billing_python_sdk.Resources.Reports.ReportsClient                            import ReportsClient
from paddle_billing_python_sdk.Resources.Subscriptions.SubscriptionsClient                import SubscriptionsClient
from paddle_billing_python_sdk.Resources.Transactions.TransactionsClient                  import TransactionsClient


class Client:
    """
    Client for making API requests using Python's requests library.
    """

    SDK_VERSION = __VERSION__


    def __init__(
        self,
        api_key:     str,             # TODO handle our api key class
        options:     Options  = None,
        http_client: Session  = None,
        logger                = None,
        retry_count: int      = 3,
    ):
        self.__api_key      = api_key
        self.retry_count    = retry_count
        self.transaction_id = None
        self.options        = options     if options     else Options()
        self.logger         = logger      if logger      else Client.null_logger()
        self.client         = http_client if http_client else self.build_request_session()

        # Initialize the various clients
        self.addresses             = AddressesClient(self)
        self.adjustments           = AdjustmentsClient(self)
        self.businesses            = BusinessesClient(self)
        self.customers             = CustomersClient(self)
        self.discounts             = DiscountsClient(self)
        self.events                = EventsClient(self)
        self.event_types           = EventTypesClient(self)
        self.notifications         = NotificationsClient(self)
        self.notification_logs     = NotificationLogsClient(self)
        self.notification_settings = NotificationSettingsClient(self)
        self.prices                = PricesClient(self)
        self.pricing_previews      = PricingPreviewsClient(self)
        self.products              = ProductsClient(self)
        self.reports               = ReportsClient(self)
        self.subscriptions         = SubscriptionsClient(self)
        self.transactions          = TransactionsClient(self)


    @staticmethod
    def null_logger() -> Logger:
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
    ) -> Response:
        """
        Makes an actual API call to Paddle
        """

        # Parse and update URI with base URL components if necessary
        if isinstance(uri, str):
            uri = urljoin(self.options.environment.base_url, uri)

        self.client.headers.update({
            'X-Transaction-ID': str(self.transaction_id) if self.transaction_id else str(uuid4())
        })

        # Serialize payload to JSON
        final_json = None
        if payload:
            json_payload  = json_dumps(payload)
            final_json    = json_payload if json_payload != '[]' else '{}'
        # self.logger.debug(f"final_json: {final_json}")

        # We use data= instead of json= because we manually serialize data into JSON
        try:
            response = self.client.request(method.upper(), uri, data=final_json)
            response.raise_for_status()

            return response
        except RequestException as e:
            if self.logger:
                self.logger.error(f"Request failed: {e}")
            raise


    @staticmethod
    def _format_uri_parameters(uri: str, parameters: HasParameters) -> str:
        if isinstance(parameters, HasParameters):
            parameters = parameters.get_parameters()

            query = urlencode(parameters)
            uri  += '&' if '?' in uri else '?'
            uri  += query

        return uri


    def get_raw(self, uri: str, parameters = None) -> Response:
        uri = Client._format_uri_parameters(uri, parameters) if parameters else uri

        return self._make_request('GET', uri, None)


    def post_raw(self, uri: str, payload: dict | None = None, parameters = None) -> Response:
        # def post_raw(self, uri: str, payload: list | dict | None = None, parameters: HasParameters | None = None):
        if payload:
            payload = FiltersUndefined.filter_undefined_values(payload)  # Strip Undefined items from the dict
        uri = Client._format_uri_parameters(uri, parameters) if parameters else uri

        return self._make_request('POST', uri, payload)


    def patch_raw(self, uri: str, payload: dict | None) -> Response:
        if payload:
            payload = FiltersUndefined.filter_undefined_values(payload)  # Strip Undefined items from the dict

        return self._make_request('PATCH', uri, payload)


    def delete_raw(self, uri: str) -> Response:
        return self._make_request('DELETE', uri)


    def build_request_session(self) -> Session:
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
