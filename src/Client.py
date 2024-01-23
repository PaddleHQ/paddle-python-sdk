import requests
import json
from urllib.parse import urlparse


# from src.Logger.Formatter                                           import CustomLogger
# from src.Entities.Addresses.AddressesClient                        import AddressesClient
# from src.Entities.Adjustment.AdjustmentsClient                    import AdjustmentsClient
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



    def request_raw(self, method, uri, payload=None):
        if isinstance(uri, str):
            components = urlparse(self.options.environment.base_url())
            uri = self.uri_factory.create_uri(uri)
            uri = uri.with_scheme(components.scheme).with_host(components.netloc)

        request = self.request_factory.create_request(method, uri)

        if payload is not None:
            body = json.dumps(payload, default=lambda o: o.__dict__)
            if body == '[]':
                body = '{}'
            request = request.with_body(self.stream_factory.create_stream(body))

        request = request.with_added_header('X-Transaction-ID', self.transaction_id or str(uuid.uuid4()))

        return self.http_client.send_async_request(request).wait()
