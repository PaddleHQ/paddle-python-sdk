import asyncio
from json import dumps as json_dumps
from logging import Logger, getLogger
from typing import Any
from urllib.parse import urljoin, urlencode
from uuid import uuid4

import httpx

from paddle_billing.Json import PayloadEncoder
from paddle_billing.Operation import Operation
from paddle_billing.HasParameters import HasParameters
from paddle_billing.Options import Options
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Logger.NullHandler import NullHandler

from paddle_billing.Resources.Addresses.AsyncAddressesClient import AsyncAddressesClient
from paddle_billing.Resources.Adjustments.AsyncAdjustmentsClient import AsyncAdjustmentsClient
from paddle_billing.Resources.Businesses.AsyncBusinessesClient import AsyncBusinessesClient
from paddle_billing.Resources.ClientTokens.AsyncClientTokensClient import AsyncClientTokensClient
from paddle_billing.Resources.Customers.AsyncCustomersClient import AsyncCustomersClient
from paddle_billing.Resources.CustomerPortalSessions.AsyncCustomerPortalSessionsClient import AsyncCustomerPortalSessionsClient
from paddle_billing.Resources.DiscountGroups.AsyncDiscountGroupsClient import AsyncDiscountGroupsClient
from paddle_billing.Resources.Discounts.AsyncDiscountsClient import AsyncDiscountsClient
from paddle_billing.Resources.Events.AsyncEventsClient import AsyncEventsClient
from paddle_billing.Resources.EventTypes.AsyncEventTypesClient import AsyncEventTypesClient
from paddle_billing.Resources.IPAddresses.AsyncIPAddressesClient import AsyncIPAddressesClient
from paddle_billing.Resources.Notifications.AsyncNotificationsClient import AsyncNotificationsClient
from paddle_billing.Resources.NotificationLogs.AsyncNotificationLogsClient import AsyncNotificationLogsClient
from paddle_billing.Resources.NotificationSettings.AsyncNotificationSettingsClient import AsyncNotificationSettingsClient
from paddle_billing.Resources.PaymentMethods.AsyncPaymentMethodsClient import AsyncPaymentMethodsClient
from paddle_billing.Resources.Prices.AsyncPricesClient import AsyncPricesClient
from paddle_billing.Resources.PricingPreviews.AsyncPricingPreviewsClient import AsyncPricingPreviewsClient
from paddle_billing.Resources.Products.AsyncProductsClient import AsyncProductsClient
from paddle_billing.Resources.Reports.AsyncReportsClient import AsyncReportsClient
from paddle_billing.Resources.Simulations.AsyncSimulationsClient import AsyncSimulationsClient
from paddle_billing.Resources.SimulationRuns.AsyncSimulationRunsClient import AsyncSimulationRunsClient
from paddle_billing.Resources.SimulationRunEvents.AsyncSimulationRunEventsClient import AsyncSimulationRunEventsClient
from paddle_billing.Resources.SimulationTypes.AsyncSimulationTypesClient import AsyncSimulationTypesClient
from paddle_billing.Resources.Subscriptions.AsyncSubscriptionsClient import AsyncSubscriptionsClient
from paddle_billing.Resources.Transactions.AsyncTransactionsClient import AsyncTransactionsClient


class AsyncClient:
    """
    Async client for making API requests using Python's httpx library.

    All resource client methods are `async def` and must be awaited:

        product = await client.products.get("pro_123")
        collection = await client.products.list()
    """

    def __init__(
        self,
        api_key: str,
        options: Options | None = None,
        http_client: httpx.AsyncClient | None = None,
        logger: Logger | None = None,
        retry_count: int = 3,
        use_api_version: int = 1,
        timeout: float = 60.0,
    ):
        self.__api_key = api_key
        self.retry_count = retry_count
        self.transaction_id = None
        self.use_api_version = use_api_version
        self.options = options if options else Options()
        self.log = logger if logger else AsyncClient.null_logger()
        self.client = http_client if http_client else self.build_async_client()
        self.timeout = timeout
        self.payload = None  # Used by pytest
        self.status_code = None  # Used by pytest

        self.addresses = AsyncAddressesClient(self)
        self.adjustments = AsyncAdjustmentsClient(self)
        self.businesses = AsyncBusinessesClient(self)
        self.client_tokens = AsyncClientTokensClient(self)
        self.customers = AsyncCustomersClient(self)
        self.customer_portal_sessions = AsyncCustomerPortalSessionsClient(self)
        self.discounts = AsyncDiscountsClient(self)
        self.discount_groups = AsyncDiscountGroupsClient(self)
        self.events = AsyncEventsClient(self)
        self.event_types = AsyncEventTypesClient(self)
        self.notifications = AsyncNotificationsClient(self)
        self.notification_logs = AsyncNotificationLogsClient(self)
        self.notification_settings = AsyncNotificationSettingsClient(self)
        self.payment_methods = AsyncPaymentMethodsClient(self)
        self.prices = AsyncPricesClient(self)
        self.pricing_previews = AsyncPricingPreviewsClient(self)
        self.products = AsyncProductsClient(self)
        self.reports = AsyncReportsClient(self)
        self.simulations = AsyncSimulationsClient(self)
        self.simulation_runs = AsyncSimulationRunsClient(self)
        self.simulation_run_events = AsyncSimulationRunEventsClient(self)
        self.simulation_types = AsyncSimulationTypesClient(self)
        self.subscriptions = AsyncSubscriptionsClient(self)
        self.transactions = AsyncTransactionsClient(self)
        self.ip_addresses = AsyncIPAddressesClient(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        await self.client.aclose()

    @staticmethod
    def null_logger() -> Logger:
        null_logger = getLogger("null_async_logger")
        null_logger.addHandler(NullHandler())
        return null_logger

    async def _logging_hook(self, response: httpx.Response) -> None:
        self.log.info(f"Request: {response.request.method} {response.request.url}")
        await response.aread()
        self.log.debug(f"Response: {response.status_code} {response.text}")

    @staticmethod
    def serialize_json_payload(payload: dict[str, Any] | Operation) -> str:
        json_payload = json_dumps(payload, cls=PayloadEncoder)
        return json_payload if json_payload != "[]" else "{}"

    async def _make_request(
        self,
        method: str,
        url: str,
        payload: dict[str, Any] | Operation | None = None,
    ) -> httpx.Response:
        if isinstance(url, str):
            url = urljoin(self.options.environment.base_url, url)

        headers = {"X-Transaction-ID": str(self.transaction_id) if self.transaction_id else str(uuid4())}
        self.payload = self.serialize_json_payload(payload) if payload else None

        retry_statuses = {429, 500, 502, 503, 504}

        for attempt in range(self.retry_count + 1):
            if attempt > 0:
                await asyncio.sleep(2 ** (attempt - 1))

            try:
                response = await self.client.request(
                    method.upper(), url, content=self.payload, headers=headers, timeout=self.timeout
                )
                self.status_code = response.status_code

                if response.status_code in retry_statuses and attempt < self.retry_count:
                    continue

                response.raise_for_status()
                return response

            except httpx.HTTPStatusError as e:
                self.status_code = e.response.status_code

                if e.response.status_code in retry_statuses and attempt < self.retry_count:
                    continue

                response_parser = ResponseParser(e.response)
                api_error = response_parser.get_error()

                if self.log:
                    self.log.error(f"Request failed: {e}.{' ' + api_error.detail if api_error is not None else ''}")

                if api_error is not None:
                    raise api_error

                raise

            except httpx.RequestError as e:
                if self.log:
                    self.log.error(f"Request failed: {e}.")

                if attempt < self.retry_count:
                    continue

                raise

        raise RuntimeError("Unexpected state in _make_request retry loop")  # pragma: no cover

    @staticmethod
    def format_uri_parameters(uri: str, parameters: HasParameters | dict[str, str]) -> str:
        if isinstance(parameters, HasParameters):
            parameters = parameters.get_parameters()

        query = urlencode(parameters)
        uri += "&" if "?" in uri else "?"
        uri += query
        return uri

    async def get_raw(self, url: str, parameters: HasParameters | dict[str, str] | None = None) -> httpx.Response:
        url = AsyncClient.format_uri_parameters(url, parameters) if parameters else url
        return await self._make_request("GET", url, None)

    async def post_raw(
        self,
        url: str,
        payload: dict[str, str] | Operation | None = None,
        parameters: HasParameters | dict[str, str] | None = None,
    ) -> httpx.Response:
        url = AsyncClient.format_uri_parameters(url, parameters) if parameters else url
        return await self._make_request("POST", url, payload)

    async def patch_raw(self, url: str, payload: dict[str, str] | Operation | None) -> httpx.Response:
        return await self._make_request("PATCH", url, payload)

    async def delete_raw(self, url: str) -> httpx.Response:
        return await self._make_request("DELETE", url)

    # --- Dispatch methods called by resource clients ---
    # Because these are `async def`, resource client methods that call them
    # return coroutines and must be awaited by callers.

    async def _get(self, url: str, params=None, parse_fn=None):
        response = await self.get_raw(url, params)
        return parse_fn(response) if parse_fn else response

    async def _post(self, url: str, payload=None, parse_fn=None, params=None):
        response = await self.post_raw(url, payload, params)
        return parse_fn(response) if parse_fn else response

    async def _patch(self, url: str, payload=None, parse_fn=None):
        response = await self.patch_raw(url, payload)
        return parse_fn(response) if parse_fn else response

    async def _delete(self, url: str, parse_fn=None):
        response = await self.delete_raw(url)
        return parse_fn(response) if parse_fn else response

    def _make_paginator(self, pagination, mapper):
        from paddle_billing.Entities.Collections.AsyncPaginator import AsyncPaginator

        return AsyncPaginator(self, pagination, mapper)

    def build_async_client(self) -> httpx.AsyncClient:
        headers = {
            "Authorization": f"Bearer {self.__api_key}",
            "Content-Type": "application/json",
            "Paddle-Version": str(self.use_api_version),
            "User-Agent": "PaddleSDK/python 1.13.0",
        }

        event_hooks: dict[str, list] = {}
        if self.log:
            event_hooks["response"] = [self._logging_hook]

        return httpx.AsyncClient(
            headers=headers,
            event_hooks=event_hooks,
        )
