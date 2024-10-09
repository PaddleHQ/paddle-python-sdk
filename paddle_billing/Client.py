from json import dumps as json_dumps, JSONEncoder
from logging import Logger, getLogger
from requests import Response, RequestException, Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin, urlencode
from uuid import uuid4
from dataclasses import fields, is_dataclass

from paddle_billing.Operation import Operation
from paddle_billing.FiltersUndefined import FiltersUndefined
from paddle_billing.Undefined import Undefined
from paddle_billing.HasParameters import HasParameters
from paddle_billing.Options import Options
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Logger.NullHandler import NullHandler

from paddle_billing.Resources.Addresses.AddressesClient import AddressesClient
from paddle_billing.Resources.Adjustments.AdjustmentsClient import AdjustmentsClient
from paddle_billing.Resources.Businesses.BusinessesClient import BusinessesClient
from paddle_billing.Resources.Customers.CustomersClient import CustomersClient
from paddle_billing.Resources.Discounts.DiscountsClient import DiscountsClient
from paddle_billing.Resources.Events.EventsClient import EventsClient
from paddle_billing.Resources.EventTypes.EventTypesClient import EventTypesClient
from paddle_billing.Resources.IPAddresses.IPAddressesClient import IPAddressesClient
from paddle_billing.Resources.Notifications.NotificationsClient import NotificationsClient
from paddle_billing.Resources.NotificationLogs.NotificationLogsClient import NotificationLogsClient
from paddle_billing.Resources.NotificationSettings.NotificationSettingsClient import NotificationSettingsClient
from paddle_billing.Resources.Prices.PricesClient import PricesClient
from paddle_billing.Resources.PricingPreviews.PricingPreviewsClient import PricingPreviewsClient
from paddle_billing.Resources.Products.ProductsClient import ProductsClient
from paddle_billing.Resources.Reports.ReportsClient import ReportsClient
from paddle_billing.Resources.Subscriptions.SubscriptionsClient import SubscriptionsClient
from paddle_billing.Resources.Transactions.TransactionsClient import TransactionsClient


class PayloadEncoder(JSONEncoder):
    def default(self, z):
        if is_dataclass(z):
            data = {}
            for field in fields(z):
                data[field.name] = getattr(z, field.name)

            return FiltersUndefined.filter_undefined_values(data)

        if isinstance(z, Undefined):
            return None

        if hasattr(z, "to_json") and callable(z.to_json):
            return z.to_json()

        return super().default(z)


class Client:
    """
    Client for making API requests using Python's requests library.
    """

    def __init__(
        self,
        api_key: str,
        options: Options = None,
        http_client: Session = None,
        logger: Logger = None,
        retry_count: int = 3,
        use_api_version: int = 1,
        timeout: float = 60.0,
    ):
        self.__api_key = api_key
        self.retry_count = retry_count
        self.transaction_id = None
        self.use_api_version = use_api_version
        self.options = options if options else Options()
        self.log = logger if logger else Client.null_logger()
        self.client = http_client if http_client else self.build_request_session()
        self.timeout = timeout
        self.payload = None  # Used by pytest
        self.status_code = None  # Used by pytest

        # Initialize the various clients
        self.addresses = AddressesClient(self)
        self.adjustments = AdjustmentsClient(self)
        self.businesses = BusinessesClient(self)
        self.customers = CustomersClient(self)
        self.discounts = DiscountsClient(self)
        self.events = EventsClient(self)
        self.event_types = EventTypesClient(self)
        self.notifications = NotificationsClient(self)
        self.notification_logs = NotificationLogsClient(self)
        self.notification_settings = NotificationSettingsClient(self)
        self.prices = PricesClient(self)
        self.pricing_previews = PricingPreviewsClient(self)
        self.products = ProductsClient(self)
        self.reports = ReportsClient(self)
        self.subscriptions = SubscriptionsClient(self)
        self.transactions = TransactionsClient(self)
        self.ip_addresses = IPAddressesClient(self)

    @staticmethod
    def null_logger() -> Logger:
        """
        Create a logger instance that logs everything to nowhere
        """

        null_logger = getLogger("null_logger")
        null_logger.addHandler(NullHandler())

        return null_logger

    def logging_hook(self, response, *args, **kwargs):
        """
        Requests logs were redirected here and to our custom logger which filters out sensitive data
        """

        self.log.info(f"Request: {response.request.method} {response.request.url}")
        self.log.debug(f"Response: {response.status_code} {response.text}")

    @staticmethod
    def serialize_json_payload(payload: dict | Operation) -> str:
        json_payload = json_dumps(payload, cls=PayloadEncoder)
        final_json = json_payload if json_payload != "[]" else "{}"

        return final_json

    def _make_request(
        self,
        method: str,
        url: str,
        payload: dict | Operation | None = None,
    ) -> Response:
        """
        Makes an actual API call to Paddle
        """
        # Parse and update URL with base URL components if necessary
        if isinstance(url, str):
            url = urljoin(self.options.environment.base_url, url)

        self.client.headers.update(
            {"X-Transaction-ID": str(self.transaction_id) if self.transaction_id else str(uuid4())}
        )

        self.payload = self.serialize_json_payload(payload) if payload else None
        try:
            # We use data= instead of json= because we manually serialize data into JSON
            response = self.client.request(method.upper(), url, data=self.payload, timeout=self.timeout)
            self.status_code = response.status_code
            response.raise_for_status()

            return response
        except RequestException as e:
            api_error = None
            if e.response is not None:
                self.status_code = e.response.status_code
                response_parser = ResponseParser(e.response)
                api_error = response_parser.get_error()

            if self.log:
                self.log.error(f"Request failed: {e}.{' ' + api_error.detail if api_error is not None else ''}")

            if api_error is not None:
                raise api_error

            raise

    @staticmethod
    def format_uri_parameters(uri: str, parameters: HasParameters | dict) -> str:
        if isinstance(parameters, HasParameters):
            parameters = parameters.get_parameters()

        query = urlencode(parameters)
        uri += "&" if "?" in uri else "?"
        uri += query

        return uri

    def get_raw(self, url: str, parameters: HasParameters | dict = None) -> Response:
        url = Client.format_uri_parameters(url, parameters) if parameters else url

        return self._make_request("GET", url, None)

    def post_raw(
        self, url: str, payload: dict | Operation | None = None, parameters: HasParameters | dict | None = None
    ) -> Response:
        if isinstance(payload, dict):
            payload = FiltersUndefined.filter_undefined_values(payload)  # Strip Undefined items from the dict

        url = Client.format_uri_parameters(url, parameters) if parameters else url

        return self._make_request("POST", url, payload)

    def patch_raw(self, url: str, payload: dict | Operation | None) -> Response:
        if isinstance(payload, dict):
            payload = FiltersUndefined.filter_undefined_values(payload)  # Strip Undefined items from the dict

        return self._make_request("PATCH", url, payload)

    def delete_raw(self, url: str) -> Response:
        return self._make_request("DELETE", url)

    def build_request_session(self) -> Session:
        session = Session()
        session.headers.update(
            {
                "Authorization": f"Bearer {self.__api_key}",
                "Content-Type": "application/json",
                "Paddle-Version": str(self.use_api_version),
                "User-Agent": "PaddleSDK/python 0.2.2",
            }
        )

        # Configure retries
        retries = Retry(total=self.retry_count, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session.mount("https://", HTTPAdapter(max_retries=retries))

        # Handle logging
        if self.log:
            session.hooks["response"] = self.logging_hook

        return session
