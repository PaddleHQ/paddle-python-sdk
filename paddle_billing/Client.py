from json import dumps as json_dumps
from re import compile as re_compile
from logging import Logger, getLogger
from requests import Response, RequestException, Session
from requests.adapters import HTTPAdapter
from typing import Any
from urllib3.util.retry import Retry
from urllib.parse import urljoin, urlencode
from uuid import UUID, uuid4
from paddle_billing.Json import PayloadEncoder as PayloadEncoder

from paddle_billing.Operation import Operation as Operation
from paddle_billing.HasParameters import HasParameters as HasParameters
from paddle_billing.Options import Options as Options
from paddle_billing.ResponseParser import ResponseParser as ResponseParser

from paddle_billing.Logger.NullHandler import NullHandler as NullHandler

from paddle_billing.Resources.Account.AccountClient import AccountClient as AccountClient
from paddle_billing.Resources.Addresses.AddressesClient import AddressesClient as AddressesClient
from paddle_billing.Resources.Adjustments.AdjustmentsClient import AdjustmentsClient as AdjustmentsClient
from paddle_billing.Resources.APIRoot.APIRootClient import APIRootClient as APIRootClient
from paddle_billing.Resources.ApiKeys.ApiKeysClient import ApiKeysClient as ApiKeysClient
from paddle_billing.Resources.Businesses.BusinessesClient import BusinessesClient as BusinessesClient
from paddle_billing.Resources.CheckoutDomains.CheckoutDomainsClient import (
    CheckoutDomainsClient as CheckoutDomainsClient,
)
from paddle_billing.Resources.ClientTokens.ClientTokensClient import ClientTokensClient as ClientTokensClient
from paddle_billing.Resources.Countries.CountriesClient import CountriesClient as CountriesClient
from paddle_billing.Resources.Currencies.CurrenciesClient import CurrenciesClient as CurrenciesClient
from paddle_billing.Resources.Customers.CustomersClient import CustomersClient as CustomersClient
from paddle_billing.Resources.CustomerPortalSessions.CustomerPortalSessionsClient import (
    CustomerPortalSessionsClient as CustomerPortalSessionsClient,
)
from paddle_billing.Resources.DiscountGroups.DiscountGroupsClient import DiscountGroupsClient as DiscountGroupsClient
from paddle_billing.Resources.Discounts.DiscountsClient import DiscountsClient as DiscountsClient
from paddle_billing.Resources.Events.EventsClient import EventsClient as EventsClient
from paddle_billing.Resources.EventTypes.EventTypesClient import EventTypesClient as EventTypesClient
from paddle_billing.Resources.IPAddresses.IPAddressesClient import IPAddressesClient as IPAddressesClient
from paddle_billing.Resources.Notifications.NotificationsClient import NotificationsClient as NotificationsClient
from paddle_billing.Resources.NotificationLogs.NotificationLogsClient import (
    NotificationLogsClient as NotificationLogsClient,
)
from paddle_billing.Resources.NotificationSettings.NotificationSettingsClient import (
    NotificationSettingsClient as NotificationSettingsClient,
)
from paddle_billing.Resources.PaymentMethods.PaymentMethodsClient import PaymentMethodsClient as PaymentMethodsClient
from paddle_billing.Resources.Prices.PricesClient import PricesClient as PricesClient
from paddle_billing.Resources.PricingPreviews.PricingPreviewsClient import (
    PricingPreviewsClient as PricingPreviewsClient,
)
from paddle_billing.Resources.Products.ProductsClient import ProductsClient as ProductsClient
from paddle_billing.Resources.Reports.ReportsClient import ReportsClient as ReportsClient
from paddle_billing.Resources.Settings.SettingsClient import SettingsClient as SettingsClient
from paddle_billing.Resources.Simulations.SimulationsClient import SimulationsClient as SimulationsClient
from paddle_billing.Resources.SimulationRuns.SimulationRunsClient import SimulationRunsClient as SimulationRunsClient
from paddle_billing.Resources.SimulationRunEvents.SimulationRunEventsClient import (
    SimulationRunEventsClient as SimulationRunEventsClient,
)
from paddle_billing.Resources.SimulationTypes.SimulationTypesClient import (
    SimulationTypesClient as SimulationTypesClient,
)
from paddle_billing.Resources.Subscriptions.SubscriptionsClient import SubscriptionsClient as SubscriptionsClient
from paddle_billing.Resources.Metrics.MetricsClient import MetricsClient as MetricsClient
from paddle_billing.Resources.Transactions.TransactionsClient import TransactionsClient as TransactionsClient
from paddle_billing.Resources.Verifications.VerificationsClient import VerificationsClient as VerificationsClient


class Client:
    """
    Client for making API requests using Python's requests library.
    """

    def __init__(
        self,
        api_key: str,
        options: Options | None = None,
        http_client: Session | None = None,
        logger: Logger | None = None,
        retry_count: int = 3,
        use_api_version: int = 1,
        timeout: float = 60.0,
    ):
        self.__api_key = api_key
        self.retry_count = retry_count
        self.transaction_id: str | UUID | None = None
        self.use_api_version = use_api_version
        self.options = options if options else Options()
        self.log = logger if logger else Client.null_logger()
        self.client = http_client if http_client else self.build_request_session()
        self.timeout = timeout
        self.payload: str | None = None  # Used by pytest
        self.status_code: int | None = None  # Used by pytest

        # Initialize the various clients
        self.account = AccountClient(self)
        self.addresses = AddressesClient(self)
        self.adjustments = AdjustmentsClient(self)
        self.api_root = APIRootClient(self)
        self.api_keys = ApiKeysClient(self, Client._get_api_key_id(api_key))
        self.businesses = BusinessesClient(self)
        self.checkout_domains = CheckoutDomainsClient(self)
        self.client_tokens = ClientTokensClient(self)
        self.countries = CountriesClient(self)
        self.currencies = CurrenciesClient(self)
        self.customers = CustomersClient(self)
        self.customer_portal_sessions = CustomerPortalSessionsClient(self)
        self.discounts = DiscountsClient(self)
        self.discount_groups = DiscountGroupsClient(self)
        self.events = EventsClient(self)
        self.event_types = EventTypesClient(self)
        self.notifications = NotificationsClient(self)
        self.notification_logs = NotificationLogsClient(self)
        self.notification_settings = NotificationSettingsClient(self)
        self.payment_methods = PaymentMethodsClient(self)
        self.prices = PricesClient(self)
        self.pricing_previews = PricingPreviewsClient(self)
        self.products = ProductsClient(self)
        self.reports = ReportsClient(self)
        self.settings = SettingsClient(self)
        self.simulations = SimulationsClient(self)
        self.simulation_runs = SimulationRunsClient(self)
        self.simulation_run_events = SimulationRunEventsClient(self)
        self.simulation_types = SimulationTypesClient(self)
        self.subscriptions = SubscriptionsClient(self)
        self.transactions = TransactionsClient(self)
        self.verifications = VerificationsClient(self)
        self.ip_addresses = IPAddressesClient(self)
        self.metrics = MetricsClient(self)

    _API_KEY_ID = re_compile(r"^pdl_\w+?_apikey_([a-z\d]{26})_")

    @staticmethod
    def _get_api_key_id(api_key: str) -> str | None:
        """Reads the ID from an API key. Returns None for keys without one, such as legacy API keys, which can't be rotated."""
        match = Client._API_KEY_ID.match(api_key or "")

        return f"apikey_{match.group(1)}" if match else None

    @staticmethod
    def null_logger() -> Logger:
        """
        Create a logger instance that logs everything to nowhere
        """

        null_logger = getLogger("null_logger")
        if not null_logger.handlers:
            null_logger.addHandler(NullHandler())

        return null_logger

    # A rotation's new_key is the full secret, and the API returns it only once.
    _SECRET_RESPONSE_FIELDS = re_compile(r'("new_key"\s*:\s*)"[^"]*"')

    def logging_hook(self, response: Response, *args: Any, **kwargs: Any) -> None:
        """
        Requests logs were redirected here and to our custom logger, with secrets redacted from response bodies
        """

        self.log.info(f"Request: {response.request.method} {response.request.url}")
        body = self._SECRET_RESPONSE_FIELDS.sub(r'\1"[REDACTED]"', response.text)
        self.log.debug(f"Response: {response.status_code} {body}")

    @staticmethod
    def serialize_json_payload(payload: dict[str, Any] | Operation) -> str:
        json_payload = json_dumps(payload, cls=PayloadEncoder)
        final_json = json_payload if json_payload != "[]" else "{}"

        return final_json

    def _make_request(
        self,
        method: str,
        url: str,
        payload: dict[str, Any] | Operation | None = None,
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
    def format_uri_parameters(uri: str, parameters: HasParameters | dict[str, str]) -> str:
        if isinstance(parameters, HasParameters):
            parameters = parameters.get_parameters()

        query = urlencode(parameters)
        uri += "&" if "?" in uri else "?"
        uri += query

        return uri

    def get_raw(self, url: str, parameters: HasParameters | dict[str, str] | None = None) -> Response:
        url = Client.format_uri_parameters(url, parameters) if parameters else url

        return self._make_request("GET", url, None)

    def post_raw(
        self,
        url: str,
        payload: dict[str, str] | Operation | None = None,
        parameters: HasParameters | dict[str, str] | None = None,
    ) -> Response:
        url = Client.format_uri_parameters(url, parameters) if parameters else url

        return self._make_request("POST", url, payload)

    def patch_raw(self, url: str, payload: dict[str, str] | Operation | None) -> Response:
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
                "User-Agent": "PaddleSDK/python 1.19.0",
            }
        )

        # Configure retries. Only urllib3's idempotent methods (GET, PUT, DELETE, etc.) are retried, never POST or PATCH.
        # 520-524 are Cloudflare origin errors.
        retries = Retry(
            total=self.retry_count,
            backoff_factor=1,
            # Return the last response once retries run out so the API error (and its Retry-After) is surfaced.
            raise_on_status=False,
            status_forcelist=[429, 500, 502, 503, 504, 520, 521, 522, 523, 524],
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))

        # Handle logging
        if self.log:
            # requests accepts a bare callable here; its stubs only allow a list
            session.hooks["response"] = self.logging_hook  # type: ignore[assignment]

        return session
